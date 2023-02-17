from django.shortcuts import render

# Create your views here.

def creer_sous_ot(request):
    return render(request, 'CreerSousOT/creer_sous_ot.html')