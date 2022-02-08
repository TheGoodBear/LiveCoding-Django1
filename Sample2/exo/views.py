from re import template
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from exo.models import Person

# Create your views here.
def Index(request):
    """
    """
    
    Persons = Person.objects.all()
    
    PersonsHTML = ""
    for MyPerson in Persons:
        PersonClass = "male" if MyPerson.sex=="m" else "female"
        PersonHTML = f"<li class='{PersonClass}'><a href='exo/{MyPerson.id}'>({MyPerson.id}) {MyPerson.name}</a></li>"
        PersonsHTML += PersonHTML

    Content = f"<ul>{PersonsHTML}</ul>"
        
    
    context = {
        "Title" : "Liste des personnes",
        "Content" : Content
    }
    
    return render(request, "exo/index.html", context)


def Detail(request, id_person):
    """
    """
    
    MyPerson = Person.objects.get(id=id_person)
    
    PersonClass = "male" if MyPerson.sex=="m" else "female"
    Content = f"<div class='{PersonClass}'>({MyPerson.id}) {MyPerson.name}</div>"
    
    context = {
        "Title" : "Détail d'une personne",
        "Content" : Content
    }

    return render(request, "exo/detail.html", context)


def IndexHTML(request):
    """
    """
    
    Persons = Person.objects.all()        
    
    context = {
        "Title" : "Liste des personnes (HTML)",
        "Persons" : Persons
    }
    
    return render(request, "exo/indexHTML.html", context)


def DetailHTML(request, id_person):
    """
    """
        
    MyPerson = Person.objects.get(id=id_person)
        
    context = {
        "Title" : "Détail d'une personne (HTML)",
        "Person" : MyPerson
    }

    return render(request, "exo/detailHTML.html", context)


class IndexGen(generic.ListView):
    """
    """
    
    template_name = "exo/indexGen.html"
    context_object_name = "Persons"
    
    def get_queryset(self):
        """
        """
        
        PersonList = Person.objects.all()
        
        # les 4 premiers triés par nom
        # PersonList = Person.objects.order_by("name")[:4]
        
        return PersonList


class DetailGen(generic.DetailView):
    """
    """
    
    template_name = "exo/detailGen.html"
    model = Person   


class CreateGen(generic.CreateView):
    """
    """
    
    template_name = "exo/createGen.html"
    model = Person
    fields = ["name", "sex"]
    success_url = "/exo/HTML/"
        

class UpdateGen(generic.UpdateView):
    """
    """
    
    template_name = "exo/updateGen.html"
    model = Person
    fields = ["name", "sex"]
    success_url = "/exo/HTML/"
    

class DeleteGen(generic.DeleteView):
    """
    """
    
    template_name = "exo/deleteGen.html"
    model = Person
    success_url = "/exo/HTML/"
