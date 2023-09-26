from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmpUser, Students, User
# Register your models here.



class CustomeUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_student',
                    'is_employee',
                    'name',
                    'surename',
                    'address',
                    'city',
                    'country',
                    'birth_date',
                    'std_pic',
                    'std_pic_pass_fro',
                    'std_pic_pass_bac'

                )
            }
        )
    )

admin.site.register(User, CustomeUserAdmin)

admin.site.register(Students)
admin.site.register(EmpUser)