# Generated by Django 4.0 on 2022-06-06 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('knowledge', '0006_skill_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]