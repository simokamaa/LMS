# Generated by Django 4.2.10 on 2024-04-21 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lms_App', '0002_menuitem_badge_menuitem_icon_menuitem_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('items', models.ManyToManyField(to='Lms_App.menuitem')),
            ],
        ),
        migrations.AlterField(
            model_name='app',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Lms_App.menuitem'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]