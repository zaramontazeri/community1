# Generated by Django 3.2.7 on 2021-09-28 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0007_auto_20210928_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to=settings.AUTH_USER_MODEL),
        ),
    ]