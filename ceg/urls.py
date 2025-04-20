from django.contrib import admin
from django.urls import path
from ceg import views  # Import the views from the ceg app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.db, name='dashboard'),
    path('tables/', views.tab, name='tables'),
    path('notifications/', views.noti, name='notifications'),
    path('Watertracking/', views.watertracking,name='Watertracking'),
    
]

