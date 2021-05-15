# Generated by Django 3.2.2 on 2021-05-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Advanced', 'Advanced'), ('Extra', 'Extra')], default=1, max_length=128),
            preserve_default=False,
        ),
    ]
