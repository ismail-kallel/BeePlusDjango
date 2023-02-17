from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from . forms import AvisForm
# Create your views here.

def correctif(request):
    return render(request,'Correctif/correctif.html')

def modifier_avis(request):
    df = pd.read_excel(r"static\excel\MOSE_IW28_N1.xlsx")
    df[["Avis"]] = df[["Avis"]].astype(str)
    df = df[df["Date de clôture"].isnull()]
    df.fillna('',inplace=True)
    df = df[df["Ordre"]!=""]
    df[["Equipement_2"]] = df[["Equipement"]].astype(str)
    df["Créé le"] = df["Créé le"].dt.date
    df_equipement = pd.read_excel(r"static\excel\machine _Mose.xlsx")
    df_equipement[["N° SAP"]] = df_equipement[["N° SAP"]].astype(str)
    df = df.merge(df_equipement, left_on="Equipement_2",right_on="N° SAP", how="left")
    df = df[["Avis", "Créé le", "Avis, heure", "Arrêt", "Description", "Equipement", "SECTION", "Ordre", "Grpe gest. PM", "Centre de coûts", "Créé par"]]
    
    df = df.rename({"Créé le":"Cree_le", "Avis, heure":"Avis_heure","Arrêt":"Arret","Grpe gest. PM":"Grpe_gest_PM","Centre de coûts":"Centre_de_couts","Créé par":"Cree_par"}, axis=1)
    
    context = {'df' : df}
    return render(request,'Correctif/modifier_avis.html',context)

def bon_pour_ot(request):
    return render(request,'Correctif/bon_pour_ot.html')

def sqcdp(request):
    return render(request,'Correctif/sqcdp.html')

def createAvis(request,pk):
    

    form = AvisForm()
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form,'pk':pk}
    return render(request, 'Correctif/avis_form.html/', context)