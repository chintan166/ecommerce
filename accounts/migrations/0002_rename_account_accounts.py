# Generated by Django 4.2.16 on 2024-12-10 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Accounts',
        ),
    ]