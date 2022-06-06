from django.contrib import admin
from dashboard.models import frgt_pwd,admin_profile,professor,student

# Register your models here.

admin.site.register(frgt_pwd)
admin.site.register(admin_profile)
admin.site.register(professor)
admin.site.register(student)

