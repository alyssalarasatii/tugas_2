from django import forms
from django.forms import ModelForm
from todolist.models import ToDoList
from todolist.models import ToDoList

class TaskForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'description')