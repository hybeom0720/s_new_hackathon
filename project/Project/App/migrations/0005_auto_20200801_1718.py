# Generated by Django 3.0.8 on 2020-08-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_merge_20200801_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', '공지사항'), ('2', '세션')], default='공지사항', max_length=10),
        ),
    ]
