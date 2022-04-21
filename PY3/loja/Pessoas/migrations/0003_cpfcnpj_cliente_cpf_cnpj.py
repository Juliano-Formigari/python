# Generated by Django 4.0.4 on 2022-04-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0002_alter_cliente_email_alter_cliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPFCNPJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default='99999999999', max_length=14, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.ForeignKey(default=99999999999, on_delete=django.db.models.deletion.CASCADE, to='Pessoas.cpfcnpj'),
            preserve_default=False,
        ),
    ]
