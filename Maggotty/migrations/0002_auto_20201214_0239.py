# Generated by Django 3.1.4 on 2020-12-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maggotty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useropinions',
            name='answers_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useropinions',
            name='answers_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useropinions',
            name='question_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useropinions',
            name='question_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
