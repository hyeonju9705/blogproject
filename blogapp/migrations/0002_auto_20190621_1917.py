# Generated by Django 2.2.1 on 2019-06-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]