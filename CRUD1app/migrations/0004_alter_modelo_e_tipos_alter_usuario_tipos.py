# Generated by Django 4.2.5 on 2024-05-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD1app', '0003_modelo_e_tipos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo_e',
            name='tipos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CRUD1app.tipo_e'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CRUD1app.tipo_e'),
        ),
    ]
