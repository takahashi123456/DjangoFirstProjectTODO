# Generated by Django 3.1.5 on 2021-02-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='dateline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='now_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
