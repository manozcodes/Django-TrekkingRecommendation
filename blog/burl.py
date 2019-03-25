from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('recommendation/', views.Recommendation, name='Recommendation'),
    path('result/', views.r_result, name='r_result'),
    # path('post/', views.post, name='post'),
    path('post/<int:id>/', views.PostDetails, name='post'),
    path('search', views.Search, name='search'),
]