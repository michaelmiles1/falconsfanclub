from django.contrib import admin
from news.models import Story

class StoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Story, StoryAdmin)
