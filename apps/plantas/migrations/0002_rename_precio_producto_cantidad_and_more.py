# Generated by Django 5.0.1 on 2024-01-25 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='id_producto',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='stock',
            new_name='valor',
        ),
    ]
