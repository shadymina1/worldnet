from django.contrib import admin

# Register your models here.
from .models import sender 
admin.site.register(sender)   

from .models import user  
admin.site.register(user)  