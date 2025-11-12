from django.urls import path

from school.views import students_list

urlpatterns = [
    path('test', students_list, name='students'),
]
