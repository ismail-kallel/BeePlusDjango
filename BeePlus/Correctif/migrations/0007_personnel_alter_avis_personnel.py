# Generated by Django 4.1.7 on 2023-02-16 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Correctif', '0006_sousensemble_alter_avis_sous_ensemble_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='avis',
            name='personnel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Correctif.personnel'),
        ),
    ]
