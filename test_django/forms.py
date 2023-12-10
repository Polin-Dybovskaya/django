from django import forms
from test_django.models import Student, Lab, Tutor


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('name', 'student', "mark")

class EditLabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('name', 'student', "mark")

'''
class EditLabForm(forms.Form):
    name = forms.CharField(help_text="Title")
    student = forms.CharField(help_text="Student")
    mark = forms.IntegerField(help_text='Mark',min_value=1, max_value=5)

'''