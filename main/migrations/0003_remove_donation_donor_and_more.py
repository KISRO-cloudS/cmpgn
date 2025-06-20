# Generated by Django 5.0.6 on 2025-06-16 07:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_add_stripe_account_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='stripe_payment_intent_id',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AddField(
            model_name='donation',
            name='transaction_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='CampaignFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_raised', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('paypal_email', models.EmailField(default='paypal_email', max_length=254)),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.campaign')),
            ],
        ),
    ]
