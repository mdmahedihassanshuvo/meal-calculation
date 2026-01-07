from django import forms
from organogram.models import Group
from member.models import Member
from django_select2.forms import Select2MultipleWidget


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'Member']
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Member': Select2MultipleWidget(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Member'].queryset = Member.objects.filter(is_member=True)
