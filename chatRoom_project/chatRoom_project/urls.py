
from django.contrib import admin
from django.urls import path,include
from chatrooms.views import IndexView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',IndexView.as_view(),name='index_page'),
    path('chat/',include("chatrooms.urls"))
    
]
