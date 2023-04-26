from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # path('', views.index.as_view(), name='index'),
    path('auto_title/', views.auto_title.as_view(), name='auto_title'),
    path('long/', views.ab_long.as_view(), name='long_ab'),
    path('short/', views.ab_short.as_view(), name='short_ab'),
    path('norm/', views.ab_norm.as_view(), name='norm_ab'),
    path('file_upload/', views.file_upload.as_view(), name='file_upload'),
    path('short_file_upload/', views.short_file_upload.as_view(), name='short_file_upload'),
    path('long_file_upload/', views.long_file_upload.as_view(), name='long_file_upload'),
    path('norm_file_upload/', views.norm_file_upload.as_view(), name='norm_file_upload'),
    path('keywords/', views.keywords.as_view(), name='keywords'),
    path('text_wrong/', views.wrong.as_view(), name='wrong'),
]
