# Generated by Django 4.0.4 on 2022-04-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_app', '0003_auto_20220416_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.TextField(),
        ),
    ]
