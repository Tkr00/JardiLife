# Generated by Django 4.0.1 on 2022-06-08 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_arbusto_flore_macetero_tierra_de_hoja_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombreP', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre Producto')),
                ('precio', models.CharField(max_length=6, verbose_name='Precio Arbusto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='flore',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='macetero',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='tierra_de_hoja',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Arbusto',
        ),
        migrations.DeleteModel(
            name='Flore',
        ),
        migrations.DeleteModel(
            name='Macetero',
        ),
        migrations.DeleteModel(
            name='Tierra_De_Hoja',
        ),
    ]
