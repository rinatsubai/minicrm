from django import forms
from minicrm.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ("Name",)
        
        
class PersonalForm(forms.ModelForm):
    class Meta:
        model = PersonalProject
        fields = ("Name", "Type", "Comment", "Links", "Deadline",)
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project       
        labels = {
            'Name': '',
            'Artist': '',
            'Status': '',
            'Price': '',
            'Prep': '',
            'Postp': '',
            'Delta': '',
            'Comment': '',
            'Start_date': '',
            'Post_date': '',
            'Deadline': '',
        }
        
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Название'},),
            'Artist': forms.Select(attrs={'class':'form-control', 'placeholder': 'Артист'}),
            'Status': forms.Select(attrs={'class':'form-control', 'placeholder': 'Статус'}),
            'Price': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Стоимость'}),
            'Prep': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Аванс'}),
            'Postp': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Постоплата'}),
            'Delta': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Остаток'}),    
            'Comment': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Коммент'}),
            'Start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Дата начала'}),
            'Post_date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Дата постоплаты'}),
            'Deadline': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Дедлайн'}),
        }
        fields = ("Name", "Artist", "Status", "Price", "Prep", "Postp", "Delta", "Start_date", "Post_date", "Deadline", "Comment")