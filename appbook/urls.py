from django.urls import path
from appbook import views

urlpatterns = [
    path('api/v1/list/', views.BookListView.as_view()),
    path('api/v1/create/', views.BookCreateView.as_view()),
    path('api/v1/update/<int:pk>/', views.BookDetailView.as_view()),
    path('', views.hello, name='hello_url'),
    path('world/', views.world, name='world_url'),

]
