# Generated by Django 4.2.2 on 2023-07-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Papeleta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='papeletaprestamo',
            name='codigo_papeleta',
            field=models.CharField(default='Null', max_length=10, unique=True),
        ),
    ]