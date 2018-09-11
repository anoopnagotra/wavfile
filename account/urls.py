from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from account import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^login/', views.userLogin, name='userLogin'),
    url(r'^fileupload/', views.fileUpload, name='fileUpload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
