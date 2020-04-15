from django.urls import path
from appbook import views

urlpatterns = [
    path('api/v1/list/', views.BookListView.as_view()),
    path('', views.hello, name='hello_url'),
    path('world/', views.world, name='world_url'),

]
