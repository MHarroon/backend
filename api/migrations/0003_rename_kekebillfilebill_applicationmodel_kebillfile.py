# Generated by Django 4.1.6 on 2023-02-18 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_bankstatment_applicationmodel_bankstatementfile_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicationmodel",
            old_name="kekeBillFilebill",
            new_name="keBillFile",
        ),
    ]
