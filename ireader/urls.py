

from django.contrib import admin
from django.urls import path

from . import view
urlpatterns = [
    path('', view.IreaderView.as_view(),name="index"),
]
