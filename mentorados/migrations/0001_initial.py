# Generated by Django 5.1.7 on 2025-04-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('estagio', models.CharField(max_length=2)),
                ('criado_em', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
