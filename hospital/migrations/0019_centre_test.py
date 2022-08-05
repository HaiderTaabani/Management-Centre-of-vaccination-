# Generated by Django 3.0.5 on 2022-04-10 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_test', models.CharField(max_length=190, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.CharField(choices=[('antigenic', 'antigenic'), ('pcr', 'pcr')], max_length=100, null=True)),
                ('resultat', models.CharField(choices=[('POSITIF', 'POSITIF'), ('NEGATIF', 'NEGATIF')], max_length=100, null=True)),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_centre', models.CharField(max_length=190, null=True)),
                ('adresse', models.CharField(max_length=190, null=True)),
                ('email', models.CharField(max_length=190, null=True)),
                ('Patient', models.ManyToManyField(to='hospital.Patient')),
            ],
        ),
    ]