from django.contrib import admin

# import Users into admin
from .models import User

admin.site.register(User)
# Register your models here.
