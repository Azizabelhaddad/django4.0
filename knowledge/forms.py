from select import select
from django import forms

from knowledge.models import Skill


Profession = (
    ('Student', 'Student'),
    ('Programmer', 'Programmer'),
    ('Devops', 'Devops'),
)
#  creation d'un model inexistant
class ContactForm(forms.Form):
    name =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), min_length=5)
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}),max_length=100)
    profession = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices=Profession)
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=5, max_length=80)
    text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows":3}),min_length=5, max_length=100)



#  creation d'un formulaire à partir d'un model
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude =["created_at", "updated_at"]

        # 2eme methode en redefinissant la method init

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# parcour du dictionaire avec .items() et modification direct des widget en ciblant la class
        for element, field in self.fields.items():    

            field.widget.attrs.update({'class': 'form-control'})


        # 1ere methode spécification avec la methode widget qui est trop lourde
        # widget = {
        # "title": forms.TextInput(attrs={"class":"form-control"}) , 
        # "experience": forms.TextInput(attrs={"class":"form-control"}), 
        # "percent": forms.NumberInput(attrs={"class":"form-control"}) , 
        # "slug": forms.TextInput(attrs={"class":"form-control"}) , 
        # "profile": forms.Select(attrs={"class":"form-control"}), 
        # "tags": forms.SelectMultiple(attrs={"class":"form-control"}),
        # "category": forms.Select(attrs={"class":"form-control"}),
        # }
        #  =["created_at", "updated_at"]
