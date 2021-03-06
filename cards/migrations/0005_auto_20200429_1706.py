# Generated by Django 3.0.5 on 2020-04-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20200427_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'card'},
        ),
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('visible', 'Visible'), ('not_visible', 'Not_visible')], default='visible', max_length=12),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_date_hapend',
            field=models.DateTimeField(),
        ),
    ]
