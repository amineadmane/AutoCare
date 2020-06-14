from django.contrib import admin
from .models import User, Admin, ChefService, ChefParc, RespMaintencance, Conducteur
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(ChefService)
admin.site.register(ChefParc)
admin.site.register(RespMaintencance)
admin.site.register(Conducteur)

