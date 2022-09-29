from django.urls import path
from todolist.views import show_todolist
from todolist.views import login_user 
from todolist.views import logout_user
from todolist.views import register
from todolist.views import task_user
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('create-task/', task_user, name='task_user'),
]