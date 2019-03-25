
from django import forms
from django.forms.widgets import NumberInput

# average trekkers walk 8 hour a day
# average walking speed 3.6 / hour 
# 1 day is equals to 28.8 km on average for walking in case of trekkers

DURATION_CHOICES = [
    (57.6, '1-2 days of trek'),
    (201.6, '3-7 days of trek'),
    (403.2, '8-14 days of trek'),
    (576, '15-20 days of trek'),
    (998, '20+ days of trek'),
]

TREKKING_CHOICES = [
    ('Cycling', 'Cycling'),
    ('Walking', 'Walking'),
    ('Biking', 'Biking'),
    ('Peak Climbing', 'Peak Climbing'),
    ('Others', 'Others'),
]

DESTINATION_CHOICES = [
    ('Adventure', 'Adventure'),
    ('Pilgrims', 'Pilgrims'),
    ('Waterbody', 'Waterbody'),
    ('Himalayas', 'Himalayas'),
    ('Nature Seeing', 'Nature Seeing'),
    ('Others', 'Others'),
]

ACCOMODATION_CHOICES = [
    ('Hotel', 'Hotel'),
    ('Pilgrims', 'Pilgrims'),
    ('Teahouse', 'Teahouse'),
    ('Motel', 'Motel'),
    ('Tent', 'Tent'),
    ('Homestay', 'Homestay'),
]

TEMPERATURE_CHOICES = [
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
]

ALTITUDE_CHOICES = [
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
]

DIFFICULTY_CHOICES = [
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
]

SECURITY_CHOICES = [
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
]

class DurationForm(forms.Form):
    duration = forms.CharField(
    widget=forms.RadioSelect(choices=DURATION_CHOICES, attrs={'class' : 'form-group radio_input icheck required '}))
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

    trekking_type = forms.CharField(
    widget=forms.RadioSelect(choices=TREKKING_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    destination_type = forms.CharField(
    widget=forms.RadioSelect(choices=DESTINATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    accomodation_type = forms.CharField(
    widget=forms.RadioSelect(choices=ACCOMODATION_CHOICES, attrs={'class' : 'form-group checkbox_input icheck required'}))

    temperature = forms.ChoiceField(choices=TEMPERATURE_CHOICES)
    altitude = forms.ChoiceField(choices=ALTITUDE_CHOICES)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
    security = forms.ChoiceField(choices=SECURITY_CHOICES)
