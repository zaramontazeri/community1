# Generated by Django 3.2.7 on 2021-09-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_rest_phone', '0010_auto_20201019_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneotp',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
