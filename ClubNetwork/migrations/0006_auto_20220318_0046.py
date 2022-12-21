# Generated by Django 3.2.6 on 2022-03-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubNetwork', '0005_auto_20220317_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='campus',
            field=models.CharField(blank=True, default='USJ', max_length=20),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='club',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='region',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
