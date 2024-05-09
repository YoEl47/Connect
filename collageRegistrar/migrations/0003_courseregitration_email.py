# Generated by Django 4.1.7 on 2023-05-26 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0002_remove_courseregitration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregitration',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]