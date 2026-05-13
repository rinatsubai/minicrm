from django.contrib import admin
from minicrm.models import *
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Created_date',)



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Artist', 'Status', 'Price', 'Prep', 'Postp', 'Prep_done', 'Postp_done', 'Delta', 'Start_date', 'Post_date', 'Deadline', 'Comment',)



class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Type', 'Links', 'Deadline', 'Comment',)
    
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(PersonalProject, PersonalProjectAdmin)
    

