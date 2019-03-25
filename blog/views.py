from django.shortcuts import render
from django.http import *
from .models import Destination
from django.db.models import Q
from .forms import DurationForm
from math import sin, cos, sqrt, atan2, radians
from scipy import spatial

#filter places radio TextInput
def FilterPlacesRadioInput(send):
    places = Destination.objects.filter(
    Q(trekking_type__contains = send['trekking']), Q(destinaton_type__contains = send['destination']), Q(accomodation_type__contains = send['accomodation'])
    )
    radiofilterplace = []
    for p in places:
        radiofilterplace.append(p.title)
    # print(radiofilterplace)
    return radiofilterplace

#Applyting cosine formula
def ApplyCosineSimi(cosine_para, places):
    # print(cosine_para)
    allnumlist = [int(x) for x in cosine_para]
    # print(allnumlist)
    data = Destination.objects.filter(title__in = places)
    result1=[]
    for d in data:
        place = [d.temperature, d.altitude, d.difficulty, d.security]
        print(place)
        result = (1 - spatial.distance.cosine(place, allnumlist)) * 100
        result1.append(float("{0:.2f}".format(result)))
    # print(result1)
    return result1

def HomePage(request):
    return render(request, 'blog/index.html')

def PostDetails(request, id):
    place = Destination.objects.get(pk=id)
    return render(request, 'blog/post.html', {"thispost": place})

def Recommendation(request):
    form = DurationForm()
    return render(request, 'blog/recommendation.html', {'form': form})

def r_result(request):
    if request.method == 'POST':
        # print('aayo')
        form = DurationForm(request.POST)
        # print(form.errors)
        # print(form.non_field_errors)
        if form.is_valid():
            # print('ok to go')
            temperature = form.cleaned_data['temperature']
            altitude = form.cleaned_data['altitude']
            difficulty = form.cleaned_data['difficulty']
            security = form.cleaned_data['security']
            trekking = form.cleaned_data['trekking_type']
            destination = form.cleaned_data['destination_type']
            accomodation = form.cleaned_data['accomodation_type']
            places = Destination.objects.all()
            hamro = form.cleaned_data['duration']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            # print(latitude)
            # print(longitude)
            data = []
            try:
                for place in places:
                    R = 6371.0
                    name = place.title
                    lat1 = radians(place.latitude)
                    lon1 = radians(place.longitude)
                    # print(latitude)
                    lat2 = radians(latitude)
                    lon2 = radians(longitude)
                    # print(lat1)

                    dlon = lon2 - lon1
                    dlat = lat2 - lat1

                    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))

                    distance = R * c

                    if distance <= int(hamro):
                        data.append(name)
            except TypeError:
                print("May be GPS is not ON. Please Trun it ON")

            finally:
                send = {'trekking':trekking, 'destination': destination, 'accomodation': accomodation}
                data_for_cosine = [temperature, altitude, difficulty, security]
                # print(data_for_cosine)
                filteredplaces = FilterPlacesRadioInput(send)
                # print(data)

                if len(data) == 0:
                    cosine_data = ApplyCosineSimi(data_for_cosine, filteredplaces)
                    finaldestination = Destination.objects.filter(title__in = filteredplaces)
                    # print(cosine_data)

                else:
                    common = set(data).intersection(set(filteredplaces))
                    # print(common)

                    cosine_data = ApplyCosineSimi(data_for_cosine, common)
                    finaldestination = Destination.objects.filter(title__in = common)
                gogo = {'places': finaldestination, 'cosine': cosine_data}
                return render(request, 'blog/r_result.html', gogo)
        else:
            form = DurationForm()
            return HttpResponseRedirect('/recommendation/')

def post(request):
    return render(request, 'blog/post.html')

def Search(request):
    return render(request, 'blog/search.html')
