# Generated by Django 4.0.6 on 2022-08-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loona', '0009_rename_state_add_state_state1'),
    ]

    operations = [
        migrations.CreateModel(
            name='s_state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.TextField()),
            ],
        ),
    ]