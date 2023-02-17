# Generated by Django 4.1.7 on 2023-02-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Correctif', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sous_ensemble_1', models.CharField(max_length=200)),
                ('sous_ensemble_2', models.CharField(max_length=200)),
                ('arret', models.BooleanField()),
                ('cloturer', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=200)),
                ('probleme', models.CharField(max_length=200)),
                ('technologie', models.CharField(choices=[('Partie Mécanique', 'Partie Mécanique'), ('Partie Electrique', 'Partie Electrique'), ('Partie Pneumatique', 'Partie Pneumatique'), ('Partie Automatiste / Asservissement', 'Partie Automatiste / Asservissement'), ('Partie Hydraulique', 'Partie Hydraulique'), ('Partie Electronique', 'Partie Electronique'), ('Partie Optique', 'Partie Optique'), ('Partie Informatique', 'Partie Informatique'), ('Partie non identifiée ou autre', 'Partie non identifiée ou autre')], max_length=200)),
                ('cause', models.CharField(choices=[("Défaut conception / fabrication de l'équipement", "Défaut conception / fabrication de l'équipement"), ("Usure / Vieillissement de l'équipement", "Usure / Vieillissement de l'équipement"), ("Déréglage de l'équipement", "Déréglage de l'équipement"), ('Mauvaise utilisation', 'Mauvaise utilisation'), ('Défaut de conception du poste de travail', 'Défaut de conception du poste de travail'), ('Défaut du procédé', 'Défaut du procédé'), ("Défaut dans l'apport extérieur d'énergie", "Défaut dans l'apport extérieur d'énergie"), ('Condition extérieure', 'Condition extérieure'), ('Pollution', 'Pollution'), ('Pollution / Obstruction / Salissure', 'Pollution / Obstruction / Salissure'), ('Défaut de maintenance', 'Défaut de maintenance'), ('Préventif', 'Préventif'), ('Cause inconnue', 'Cause inconnue')], max_length=200)),
                ('groupe_gestionnaire', models.CharField(choices=[('E16', 'E16'), ('E17', 'E17'), ('E18', 'E18'), ('E05', 'E05'), ('E19', 'E19'), ('E23', 'E23'), ('E10', 'E10')], max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Mose_iw28_N1',
        ),
    ]