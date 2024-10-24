# Generated by Django 5.1.2 on 2024-10-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programsdir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the director name', max_length=255)),
                ('address', models.CharField(help_text='Enter the director address', max_length=100)),
                ('phone', models.CharField(help_text='Enter the director phone number', max_length=12)),
                ('email', models.EmailField(help_text='Enter the director email', max_length=100)),
            ],
            options={
                'verbose_name': 'programsdir',
                'verbose_name_plural': 'programsdir',
            },
        ),
    ]
