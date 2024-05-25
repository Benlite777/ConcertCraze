from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('songs/', views.song_list, name='song_list'),
    path('art/',views.art,name='art'),
    path('concert/',views.concert,name='concert'),
    
    
]




