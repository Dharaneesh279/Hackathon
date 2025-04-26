from django.contrib import admin
from django.urls import path
from ceg import views  # Import the views from the ceg app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.db, name='dashboard'),
    path('tables/', views.tab, name='tables'),
    path('notifications/', views.noti, name='notifications'),
    path('Watertracking/', views.watertracking, name='Watertracking'),
    path('', views.login, name='login'),  # Default login+signup page
    path('logout/', views.logout, name='logout'),  # Logout route
    path('profile1/', views.profile1, name='profile1'),
    path('waterbilling/', views.waterbilling, name='waterbilling'),
]
