from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'start_date')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-start_date',)
    readonly_fields = ('start_date',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('start_date', 'about')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1',
                       'password2', 'is_staff', 'is_active')
        }),
    )

    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})}
    }


admin.site.register(CustomUser, UserAdminConfig)
