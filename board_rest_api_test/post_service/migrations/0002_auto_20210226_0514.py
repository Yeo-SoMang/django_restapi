# Generated by Django 3.1.7 on 2021-02-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('regdate',)},
        ),
    ]