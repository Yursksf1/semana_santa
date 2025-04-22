from django.contrib import admin

# Register your models here.
from myapp.models import Video
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Video, VideoAdmin)