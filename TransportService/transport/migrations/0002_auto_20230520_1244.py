# Generated by Django 3.2.12 on 2023-05-20 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rider',
            name='gender',
        ),
        migrations.CreateModel(
            name='Sechdule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.DateTimeField(blank=True, null=True)),
                ('tuesday', models.DateTimeField(blank=True, null=True)),
                ('wednesday', models.DateTimeField(blank=True, null=True)),
                ('thursday', models.DateTimeField(blank=True, null=True)),
                ('friday', models.DateTimeField(blank=True, null=True)),
                ('saturday', models.DateTimeField(blank=True, null=True)),
                ('sunday', models.DateTimeField(blank=True, null=True)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.rider')),
            ],
        ),
    ]