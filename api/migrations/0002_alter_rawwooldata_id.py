# Generated by Django 4.2.5 on 2023-09-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawwooldata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]