# Generated by Django 5.0.6 on 2025-06-21 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_posterslide_campaign_motion_poster_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='poster_slides',
        ),
        migrations.AddField(
            model_name='posterslide',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster_slides', to='main.campaign'),
        ),
    ]
