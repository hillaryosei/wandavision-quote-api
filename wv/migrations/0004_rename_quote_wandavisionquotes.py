# Generated by Django 4.1.1 on 2022-09-14 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wv', '0003_quote_delete_wvquotes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quote',
            new_name='wandaVisionQuotes',
        ),
    ]
