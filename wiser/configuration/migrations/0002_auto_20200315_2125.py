# Generated by Django 2.2.10 on 2020-03-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('facebook', 'fa-facebook-f'), ('google-plus', 'fa-google-plus-g'), ('linkedin', 'fa-linkedin-in'), ('instagram', 'fa-instagram')], max_length=20),
        ),
    ]
