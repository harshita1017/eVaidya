# Generated by Django 3.0.5 on 2022-06-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Medical Consultants', 'Medical Consultants'), ('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Physician', 'Physician')], default='Cardiologist', max_length=50),
        ),
    ]
