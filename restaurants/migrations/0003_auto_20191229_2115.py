# Generated by Django 3.0.1 on 2019-12-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20191229_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(blank=True, max_length=300, upload_to='Place/static/locals/img', verbose_name='Zdjęcie'),
        ),
    ]
