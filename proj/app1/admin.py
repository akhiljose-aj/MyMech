from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(users)
admin.site.register(mechanic)
admin.site.register(book_service)
admin.site.register(accept_serv)
admin.site.register(admin_log)
admin.site.register(user_contact)
admin.site.register(mech_contact)
