# Generated by Django 5.1.2 on 2024-10-15 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0003_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='prueba.generos'),
        ),
    ]
