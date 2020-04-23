# Generated by Django 3.0.5 on 2020-04-23 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_date',
            new_name='card_date_short',
        ),
        migrations.AddField(
            model_name='card',
            name='card_date_long',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]