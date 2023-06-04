from django.contrib import admin
from .models import Category, Tool, About, Post, SocialLink, ProfileData, Projects, Service

admin.site.register(About)
admin.site.register(Projects)
admin.site.register(SocialLink)
admin.site.register(ProfileData)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Tool)
