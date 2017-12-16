from django.conf.urls import url
from . import views

app_name = 'music'


urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='registration'),
    # music/'any_number'/
    url(r'^(?P<pk>\d+)/$', views.DetailsView.as_view(), name='detail'),
    #music/album/add
    url(r'^album/add$', views.AlbumCreate.as_view(),name='album_add'),
    #music/album/add
    url(r'^(?P<pk>\d+)/update$', views.AlbumUpdate.as_view(),name='album_update'),
    #music/album/add
    url(r'^(?P<pk>\d+)/delete$', views.AlbumDelete.as_view(),name='album_delete')
]
