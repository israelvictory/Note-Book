# Generated by Django 3.0.7 on 2020-06-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(max_length=20, verbose_name='list of categories'),
        ),
    ]
