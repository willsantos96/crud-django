# Generated by Django 4.0.1 on 2022-02-03 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='sobrenomenome',
            new_name='sobrenome',
        ),
    ]
