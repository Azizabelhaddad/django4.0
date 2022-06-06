from http.client import HTTPResponse
from django.shortcuts import render,redirect

from knowledge.models import Skill
from .forms import ContactForm, SkillForm

from django.http import HttpResponse

# Create your views here.

knows = Skill.objects.all()

def list_knowledge(request):
    return render(request, 'knowledge/index.html', {"knows": knows})


def get_knowledge(request, id):
    skill = Skill.objects.get(pk=id)
    return render(request, 'knowledge/showSkill.html', {"skill":skill})

def contact(request):

    #  la methode de validation du formulaire est la meme que celle du traiteent du formulaire

    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            # cleaned_data contien un dictionaire des donnes valides
           print(form_contact.cleaned_data)
    else:

        #  la partie get 
        form_contact = ContactForm()

    return render(request, 'knowledge/contact.html', {"form": form_contact})

def createSkill(request):

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("skill-list")
    else:
        form = SkillForm()


    return render(request, 'knowledge/createSkill.html', {"form": form})

def editeSkill(request, id):
    skill = Skill.objects.get(pk=id)
    
    if request.method == "POST":
        form = SkillForm(request.POST, instance= skill)
        if form.is_valid():
            form.save()
            return redirect("skill-list")

    else:
        # lors du get il charge lobject à modifier
        form = SkillForm(instance=skill)


    return render(request, 'knowledge/editeSkill.html', {"form": form})


def deleteSkill(request, id):
    skill = Skill.objects.get(pk=id)
    
    if request.method == "POST":
        skill.delete()
        return redirect("skill-list")


    return render(request, 'knowledge/deleteSkill.html', {"skill": skill})

