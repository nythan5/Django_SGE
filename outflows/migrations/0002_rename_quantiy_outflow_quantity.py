# Generated by Django 5.0.7 on 2024-07-17 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outflow',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]
