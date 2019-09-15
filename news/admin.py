from django.contrib import admin
from news.models import Story, Category

class StoryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)
