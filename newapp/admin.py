
from django.contrib import admin

from .models import *

admin.site.register(activeusers)
admin.site.register(loggedinusers)
admin.site.register(organization)

