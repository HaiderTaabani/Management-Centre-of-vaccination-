# Generated by Django 3.0.5 on 2022-04-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_centre_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
        migrations.AddField(
            model_name='doctor',
            name='centre',
            field=models.CharField(choices=[('Centre Constantine', 'Centre Constantine'), ('centre Annaba', 'Centre Annaba'), ('Centre Alger', 'Centre Alger'), ('Centre Skikda', 'Centre Skikda'), ('Centre Batna', 'Centre Batna'), ('Centre oran', 'Centre oran'), ('Centre mila', 'Centre Mila')], default='Constantine', max_length=50),
        ),
        migrations.DeleteModel(
            name='Centre',
        ),
    ]