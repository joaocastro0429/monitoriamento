# Generated by Django 5.1.7 on 2025-04-03 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0003_alter_mentorados_user_alter_navigators_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorados',
            name='navigator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentorados.navigators'),
        ),
    ]
