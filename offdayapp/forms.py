from django import forms
from .models import TeamMember, OffDay

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name']

class OffDayForm(forms.ModelForm):
    type = forms.ChoiceField(choices=OffDay.OFFDAY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = OffDay
        fields = ['team_member', 'day', 'type']
