# Generated by Django 3.0.2 on 2020-02-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200215_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='password2',
        ),
        migrations.AlterField(
            model_name='voter',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='voter',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
