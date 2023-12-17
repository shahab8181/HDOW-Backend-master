# Generated by Django 4.2.7 on 2023-12-01 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_echo_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='echo',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='echos', to=settings.AUTH_USER_MODEL),
        ),
    ]