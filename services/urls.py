from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),            # Homepage
    path('login/', views.login_view, name='login'),
    path('wedding/', views.wedding_page, name='wedding'),
    path('venue/', views.venue_page, name='venue'),
    path('venue/venue1/', views.venue1_page, name='venue1'),
    path('api/services/', views.get_services, name='get_services'),
    path('api/venue/', views.get_venue, name='get_venue'),
    path('api/add-venue/', views.add_venue, name='add_venue'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]
