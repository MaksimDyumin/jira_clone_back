# Generated by Django 4.2 on 2023-04-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira_rest', '0004_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
