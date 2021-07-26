from .models import Student

from django import forms

from datetime import date


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))



