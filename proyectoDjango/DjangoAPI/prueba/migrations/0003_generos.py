# Generated by Django 5.1.2 on 2024-10-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_alter_usuarios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='generos',
            fields=[
                ('genero_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
    ]
