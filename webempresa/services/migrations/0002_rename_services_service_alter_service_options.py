# Generated by Django 5.0.4 on 2024-05-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
