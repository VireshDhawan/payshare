# Generated by Django 2.2.5 on 2019-09-12 20:43

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('purchases', '0019_userprofile_paypal_me_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='collective',
            name='logo_url',
            field=filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_collective', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
