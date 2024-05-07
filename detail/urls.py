from django.urls import path
from .views import List_home_view, Post_detail,Logout_view

urlpatterns=[
    path('',List_home_view.as_view(),name='home'),
    path('<int:pk>',Post_detail.as_view(), name='detail'),
    path('logout/',Logout_view, name = 'logout'),
]