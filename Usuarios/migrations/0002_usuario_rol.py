# Generated by Django 4.2.2 on 2023-07-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
