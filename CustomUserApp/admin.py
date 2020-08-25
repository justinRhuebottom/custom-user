from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from CustomUserApp.models import MyUser

UserAdmin.fieldsets += (
        ('Custom Fields', {
            'fields': ('display_name', 'homepage', 'age'),
        }),
    )

admin.site.register(MyUser, UserAdmin)