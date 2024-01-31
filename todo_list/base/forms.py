from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Todos


class AddTodo(ModelForm):
    class Meta:
        model = Todos
        fields = ['name', 'description',]