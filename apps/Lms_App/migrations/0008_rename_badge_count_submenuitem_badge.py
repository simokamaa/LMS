# Generated by Django 4.2.10 on 2024-05-06 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lms_App', '0007_rename_badge_count_menuitem_badge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submenuitem',
            old_name='badge_count',
            new_name='badge',
        ),
    ]
