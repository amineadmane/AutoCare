# Generated by Django 3.0.4 on 2020-06-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChefService',
            new_name='CentralUser',
        ),
        migrations.RenameModel(
            old_name='ChefParc',
            new_name='OperationnelUser',
        ),
        migrations.RenameModel(
            old_name='Conducteur',
            new_name='RegionalUser',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'admin'), (1, 'Operationnel'), (2, 'Regional'), (3, 'Central')]),
        ),
        migrations.DeleteModel(
            name='RespMaintencance',
        ),
    ]
