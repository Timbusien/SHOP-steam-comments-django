# Generated by Django 4.2.5 on 2023-10-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='img',
            field=models.FileField(upload_to='stor'),
        ),
    ]