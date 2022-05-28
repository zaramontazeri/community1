# Generated by Django 3.2.7 on 2021-09-29 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0005_auto_20210929_0526'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0008_alter_condition_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='info_gallery_images', to='media_app.image'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='auth_rest_phone.userprofile'),
            preserve_default=False,
        ),
    ]