from django.urls import path
from .views import IndexView,TodoDetail

app_name = 'todo'

urlpatterns = [
    path('tasks/', IndexView.as_view()),
    path('tasks/<int:pk>/', TodoDetail.as_view()),

]