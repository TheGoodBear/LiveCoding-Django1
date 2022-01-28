from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    Persons = [
        {"name" : "Tim",
         "sex" : "m"},
        {"name" : "Adrien",
         "sex" : "m"},
        {"name" : "David",
         "sex" : "o"},
        {"name" : "Nico",
         "sex" : "m"},
        {"name" : "Cécilia",
         "sex" : "f"},
        {"name" : "Théo",
         "sex" : "m"},
        {"name" : "Sophie",
         "sex" : "f"},
        ]
    
    PersonHTML = ""
    for Person in Persons:
        CSSClass = "male"
        if Person["sex"] == "f":
            CSSClass = "female"
        elif Person["sex"] == "o":
            CSSClass = "other"
        PersonHTML += f"<li class='{CSSClass}'>{Person['name']}</li>"
    ContentHTML = f"<ul>{PersonHTML}</ul>"
 
    
    context = {
        "CSSFile" : "live1/index.css",
        "PageTitle" : "Accueil",
        "Title" : "Liste des personnes",
        "Content" : ContentHTML
    }

    
    return render(request, "live1/index.html", context)
