# Generated by Django 3.2.4 on 2021-07-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210702_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='usr_password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]