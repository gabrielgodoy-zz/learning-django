from django.conf.urls import url
from . import views  # imports views file

# App music namespace
app_name = 'music'

# as_view | Treat view classes as a view
urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),  # Homepage of the music section, empty regex matches all

    # The ?P is a named capturing group. creates a match group named album_id
    # /music/<primary_key>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ^ is the beginning
    # $ is the end

    # URL for creating a new object (album)
    # music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # music/album/<primary_key>/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/<primary_key>/delete
    url(r'(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


    # register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
