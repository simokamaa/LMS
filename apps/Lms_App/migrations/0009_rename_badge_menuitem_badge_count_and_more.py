# Generated by Django 4.2.10 on 2024-05-07 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lms_App', '0008_rename_badge_count_submenuitem_badge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='badge',
            new_name='badge_count',
        ),
        migrations.RenameField(
            model_name='submenuitem',
            old_name='badge',
            new_name='badge_count',
        ),
    ]
