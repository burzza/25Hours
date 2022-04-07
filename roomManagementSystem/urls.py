from unicodedata import name
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path("roomAdd",views.addRoom, name="roomAdd"),
    path("details",views.room, name="rm"),
    path('search',views.searchbar, name="search"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)