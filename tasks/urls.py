from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tasks'

urlpatterns = [
    url('index/', views.index, name='index'),
    url(r'^deleteTask/(?P<id>[0-9]+)/', views.deleteTask, name='deleteTask'),
    url(r'^addTask/', views.addTask, name='addTask'),
    url(r'^getEditTask/(?P<id>[0-9]+)/', views.getEditTask, name='getEditTask'),
    url(r'^editTask/', views.editTask, name='editTask'),
    url(r'^markCompleted/(?P<id>[0-9]+)/', views.markCompleted, name='markCompleted')
    #url(r'^createTask/', views.createTask, name='createTask')
]