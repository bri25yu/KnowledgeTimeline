# Generated by Django 2.2.8 on 2022-03-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_node_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='authors',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]