# Generated by Django 3.2.8 on 2021-10-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videojuegos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]