from django.contrib import admin
from .models import User, Admin, OperationnelUser, CentralUser, RegionalUser
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(OperationnelUser)
admin.site.register(RegionalUser)
admin.site.register(CentralUser)
