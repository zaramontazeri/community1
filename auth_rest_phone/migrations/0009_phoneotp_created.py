# Generated by Django 3.1.2 on 2020-10-17 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_rest_phone', '0008_auto_20201017_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]