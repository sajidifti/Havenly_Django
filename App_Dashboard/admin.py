from django.contrib import admin
from App_Dashboard.models import Country, DesignerInfo, Post, ContactUs, AboutUs, React, Reply, DesignerMessage

# Register your models here.

admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(React)