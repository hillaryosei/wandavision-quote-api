# Generated by Django 4.1.1 on 2022-09-14 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wvquotes',
            old_name='name',
            new_name='speaker',
        ),
    ]