from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('more/<int:sample_id>',views.more,name = "more"),
    path('turnonoff/',views.turnonoff,name = "turnonoff"),
    path('restapi/', views.restapi, name="restapi"),
    path('restapi1/', views.restapi1, name="restapi1"),
]
