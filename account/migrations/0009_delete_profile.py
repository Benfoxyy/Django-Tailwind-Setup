# Generated by Django 4.2.14 on 2024-12-01 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_is_active_alter_user_is_superuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
