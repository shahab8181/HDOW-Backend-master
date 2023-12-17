# Generated by Django 4.2.7 on 2023-12-01 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_case_technician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='technician',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_technicians', to=settings.AUTH_USER_MODEL),
        ),
    ]