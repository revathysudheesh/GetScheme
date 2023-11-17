# Generated by Django 4.2.6 on 2023-10-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schemesdb',
            old_name='Type',
            new_name='Type1',
        ),
        migrations.AddField(
            model_name='schemesdb',
            name='Type2',
            field=models.CharField(blank=True, choices=[('Disabilty', 'Disability'), ('Reservation', 'Reservation'), ('Profession', 'Profession'), ('State', 'State'), ('Insurance', 'Insurance'), ('General', 'General')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='schemesdb',
            name='Type3',
            field=models.CharField(blank=True, choices=[('Disabilty', 'Disability'), ('Reservation', 'Reservation'), ('Profession', 'Profession'), ('State', 'State'), ('Insurance', 'Insurance'), ('General', 'General')], max_length=50, null=True),
        ),
    ]
