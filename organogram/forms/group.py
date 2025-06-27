from django import forms
from organogram.models import Group
from django_select2.forms import Select2MultipleWidget


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'Member']
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Member': Select2MultipleWidget(attrs={'class': 'form-control'}),
        }
