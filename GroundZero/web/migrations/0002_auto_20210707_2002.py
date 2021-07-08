# Generated by Django 3.2.4 on 2021-07-08 00:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proovedor',
            name='moneda',
            field=models.CharField(default=1, max_length=7, verbose_name='Moneda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proovedor',
            name='contra',
            field=models.CharField(max_length=8, verbose_name='Contrasenna'),
        ),
        migrations.AlterField(
            model_name='proovedor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]