# Generated by Django 4.2.7 on 2023-11-09 12:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200, verbose_name='Header')),
                ('text', tinymce.models.HTMLField(max_length=5000, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Text information',
                'verbose_name_plural': 'Texts information',
            },
        ),
    ]
