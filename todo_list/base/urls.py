from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo_view, name='todo'),
    path('addtodo/', views.add_view, name='addtodo'),
    path('update/<str:pk>/', views.update_view, name='update'),
    path('delete/<str:pk>/', views.delete_view, name='delete')
]
