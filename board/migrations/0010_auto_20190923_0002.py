# Generated by Django 2.2.3 on 2019-09-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20190922_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.FileField(default='https://image.flaticon.com/icons/svg/149/149852.svg', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='missing',
            name='image',
            field=models.FileField(default='https://image.flaticon.com/icons/svg/149/149852.svg', upload_to='missing_images/%Y/%m/%d'),
        ),
    ]