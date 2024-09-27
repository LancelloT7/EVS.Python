# Generated by Django 5.1.1 on 2024-09-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.EmailField(max_length=254, verbose_name='Email')),
                ('senha', models.CharField(max_length=64, verbose_name='Senha')),
                ('campo_teste', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
