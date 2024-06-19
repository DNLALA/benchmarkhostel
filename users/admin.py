from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('email', 'reg_no', 'is_student', 'is_warden', 'is_staff', 'is_active', 'has_hostel', 'gender')
    list_filter = ('is_student', 'is_warden', 'is_staff', 'is_active', 'has_hostel', 'gender')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('reg_no', 'gender',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_student', 'is_warden', 'has_hostel')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'reg_no', 'password1', 'password2', 'is_student', 'is_warden', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'reg_no')
    ordering = ('email',)

# Register the custom UserAdmin class with the User model
admin.site.register(User, UserAdmin)
