from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name=""),
]
