# Generated by Django 4.0.4 on 2022-04-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='Cliente',
        ),
    ]