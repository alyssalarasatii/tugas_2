from django import forms
from django.forms import ModelForm
from todolist.models import ToDoList
from todolist.models import ToDoList

class TaskForm(forms.Form):
    class Meta:
        model = ToDoList
        fields = ('title', 'description')
