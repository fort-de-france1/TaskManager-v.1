from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                "class": "radius",
                "placeholder": "Task name"
            }),
            "text": Textarea(attrs={
                "class": "radius",
                "placeholder": "Task description"

            })

        }