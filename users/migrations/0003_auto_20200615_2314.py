# Generated by Django 3.0.4 on 2020-06-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200614_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dateEmbauche',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dateNaissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nss',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.PositiveSmallIntegerField(choices=[(1, 'region-1'), (2, 'region-2'), (3, 'region-3'), (4, 'region-4'), (5, 'region-5'), (6, 'region-6')], default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='service',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unite',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
