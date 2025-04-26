from django.contrib import admin
from .models import UserProfile  # Import your model

# Register your model so it appears in the admin panel
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # You can add more fields here if needed
