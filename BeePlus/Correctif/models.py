from django.db import models

# Create your models here.

class SousEnsemble(models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom



class Avis(models.Model):
    TECHNOLOGIE_CHOICES = [
        ("Partie Mécanique","Partie Mécanique"),
        ("Partie Electrique","Partie Electrique"),
        ("Partie Pneumatique","Partie Pneumatique"),
        ("Partie Automatiste / Asservissement","Partie Automatiste / Asservissement"),
        ("Partie Hydraulique","Partie Hydraulique"),
        ("Partie Electronique","Partie Electronique"),
        ("Partie Optique", "Partie Optique"),
        ("Partie Informatique","Partie Informatique"),
        ("Partie non identifiée ou autre","Partie non identifiée ou autre")
    ]
    CAUSE_CHOICES = [
        ("Défaut conception / fabrication de l'équipement","Défaut conception / fabrication de l'équipement"),
        ("Usure / Vieillissement de l'équipement","Usure / Vieillissement de l'équipement"),
        ("Déréglage de l'équipement","Déréglage de l'équipement"),
        ("Mauvaise utilisation","Mauvaise utilisation"),
        ("Défaut de conception du poste de travail","Défaut de conception du poste de travail"),
        ("Défaut du procédé","Défaut du procédé"),
        ("Défaut dans l'apport extérieur d'énergie","Défaut dans l'apport extérieur d'énergie"),
        ("Condition extérieure","Condition extérieure"),
        ("Pollution","Pollution"),
        ("Pollution / Obstruction / Salissure","Pollution / Obstruction / Salissure"),
        ("Défaut de maintenance","Défaut de maintenance"),
        ("Préventif","Préventif"),
        ("Cause inconnue","Cause inconnue")
    ]

    GRP_GEST_CHOICES = [
        ("E16","E16"),
        ("E17","E17"),
        ("E18","E18"),
        ("E05","E05"),
        ("E19","E19"),
        ("E23","E23"),
        ("E10","E10")
    ]

    CLOTURER_CHOICES = [
        ("Oui","Oui"),
        ("Non","Non")
    ]

    
    
    sous_ensemble_1 = models.ForeignKey(SousEnsemble, on_delete=models.SET_NULL, null=True, related_name='sous_ensemble_1')
    sous_ensemble_2 = models.ForeignKey(SousEnsemble, on_delete=models.SET_NULL, null=True, related_name='sous_ensemble_2')
    arret = models.BooleanField()
    cloturer = models.CharField(max_length=200, choices=CLOTURER_CHOICES)
    probleme = models.CharField(max_length=200)
    
    technologie = models.CharField(max_length=200, choices=TECHNOLOGIE_CHOICES)
    cause = models.CharField(max_length=200, choices=CAUSE_CHOICES)
    groupe_gestionnaire = models.CharField(max_length=200,choices=GRP_GEST_CHOICES)


    probleme = models.CharField(max_length=300)
    action = models.CharField(max_length = 300)
    reste_a_faire = models.CharField(max_length=300)


    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL,null=True)
    date = models.DateField()
    dht = models.IntegerField()


    