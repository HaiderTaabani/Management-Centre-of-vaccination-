# Generated by Django 3.0.5 on 2022-04-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0024_vaccination_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='marque',
            field=models.CharField(choices=[('Pfizer', 'Pfizer'), (' AstraZeneka ', 'AstraZeneka '), ('Spoutnik', 'Spoutnik')], max_length=190, null=True),
        ),
    ]