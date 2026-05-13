from django.urls import path
from minicrm import views
from minicrm.models import *

artist_list_view = views.ArtistListView.as_view(
    queryset=Artist.objects.all(),
    context_object_name="artist_list",
    template_name="minicrm/artist_list.html",
)

personal_project_list_view = views.PersonalProjectListView.as_view(
    queryset=PersonalProject.objects.all(),
    context_object_name="pproject_list",
    template_name="minicrm/personal.html",
)

urlpatterns = [
    path("", views.project_list, name="minicrm"),
    path("minicrm/", views.project_list, name='minicrm'),
    path("personal/", personal_project_list_view, name="personal"),
    path("addproject/", views.add_project, name="addproject"),
    path("editproject/<str:pk>", views.edit_project, name="editproject"),
    path("addartist/", views.add_artist, name="addartist"),
    path("addpersonal/", views.add_personal, name="addpersonal"),
    path("artists/", artist_list_view, name="artistlist"),
]

