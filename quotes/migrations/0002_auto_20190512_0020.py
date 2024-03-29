# Generated by Django 2.2 on 2019-05-12 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='jobfile',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='sitestatus',
            field=models.CharField(choices=[('EX', 'Existing Site'), ('NEW', 'New Site')], max_length=20),
        ),
    ]
