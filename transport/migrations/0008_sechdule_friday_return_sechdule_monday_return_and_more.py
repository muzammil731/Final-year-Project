# Generated by Django 4.2.1 on 2023-06-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0007_alter_riderequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sechdule',
            name='friday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='monday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='saturday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='sunday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='thursday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='tuesday_return',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sechdule',
            name='wednesday_return',
            field=models.TimeField(blank=True, null=True),
        ),
    ]