# Generated by Django 4.2.1 on 2023-05-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0003_alter_empmst_edept_alter_empmst_orgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmst',
            name='edept',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empmst',
            name='orgid',
            field=models.IntegerField(null=True),
        ),
    ]