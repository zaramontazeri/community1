# Generated by Django 3.2.7 on 2021-09-26 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_condition_insurance_from_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='insurance_date',
            new_name='insurance_to_date',
        ),
        migrations.RemoveField(
            model_name='info',
            name='blood',
        ),
    ]
