from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAddForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email',
                  'first_name',
                  'last_name',
                  'password',
                  'is_active',
                  'is_staff')


class AccountAdmin(UserAdmin):
    add_form = AccountAddForm
    list_display = ('email',
                    'first_name',
                    'last_name',
                    'last_login',
                    'date_joined',
                    'is_active',
                    'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'first_name',
                       'last_name',
                       'password',
                       'is_active',
                       'is_staff')
        }),
    )

    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
