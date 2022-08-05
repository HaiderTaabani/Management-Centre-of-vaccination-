# Generated by Django 3.0.5 on 2022-04-17 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_auto_20220416_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacc_id', models.CharField(max_length=190, null=True)),
                ('marque', models.CharField(max_length=190, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient')),
            ],
            options={
                'verbose_name': 'Table vaccination',
                'verbose_name_plural': 'Table vaccination',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
