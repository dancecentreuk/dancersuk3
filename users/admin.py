from django.contrib import admin
from .models import Account, Profile, CompanyProfile, DancersProfile, DancerImage, Customer
from django.contrib.auth.admin import UserAdmin


class MyAdminAccounts(UserAdmin):
    model = Account

    list_display = ('email', 'first_name', 'last_name',  'is_active')
    list_filter = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name')
    readonly_fields = ['date_joined']


    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'first_name', 'last_name', 'password1', 'password2', )
        }),
    )

    fieldsets = (
        (None, {'fields': ('email','first_name', 'last_name', 'password')}),
        ('permissions', {'fields':('is_staff', 'is_active', )})
    )


admin.site.register(Account, MyAdminAccounts)
admin.site.register(Profile)
admin.site.register(DancersProfile)
admin.site.register(CompanyProfile)
admin.site.register(DancerImage)
admin.site.register(Customer)

