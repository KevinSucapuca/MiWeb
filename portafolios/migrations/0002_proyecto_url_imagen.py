# Generated by Django 4.2.4 on 2023-08-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='url_imagen',
            field=models.URLField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]