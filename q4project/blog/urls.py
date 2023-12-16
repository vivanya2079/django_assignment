from django.urls import path
from.views import LoginCreate,LoginList,LoginUpdateView,LoginDeleteView


urlpatterns=[
     path('login/create',LoginCreate.as_view() ,name='login_create'),
     path('login/list',LoginList.as_view(),name='login_list'),
     path('login/update/<int:pk>/',LoginUpdateView.as_view(),name='login_update'),
     path('login/delete/<int:pk>/',LoginDeleteView.as_view(),name='login_delete'),
]