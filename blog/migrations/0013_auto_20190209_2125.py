# Generated by Django 2.1.4 on 2019-02-09 15:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190202_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
