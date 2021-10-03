from django.contrib import admin
from django.urls import path, include
from courses.views import home
from courses.views import coursePage
from django.conf.urls.static import static
from learnakash.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('', home, name='homepage'),
    path('course/<str:slug>', coursePage, name='coursePage')
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
