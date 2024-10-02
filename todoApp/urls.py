from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/update/", views.UpdateView.as_view(), name='update'),
    path("<int:pk>/delete/", views.DeleteView.as_view(), name='delete'),
]