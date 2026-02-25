from django.contrib import admin
from .models import Course, Registration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title',)
    list_editable = ('is_active',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course', 'training_format', 'status', 'created_at')
    list_filter = ('status', 'training_format', 'course')
    search_fields = ('full_name', 'email')
    fieldsets = (
        ('Student Information', {
            'fields': ('full_name', 'email', 'phone_number')
        }),
        ('Training Selection', {
            'fields': ('course', 'training_format', 'message')
        }),
        ('Administrative', {
            'fields': ('status', 'created_at')
        }),
    )
    readonly_fields = ('created_at',)
