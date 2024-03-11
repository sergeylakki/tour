from django.urls import path
from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>',  views.EventDetailView.as_view(), name='event'),
    path('about', views.AboutUsView.as_view(), name='about_us'),
    path('reservation', views.ReservationCreateView.as_view(), name='reservation')
]

