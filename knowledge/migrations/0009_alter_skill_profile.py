# Generated by Django 4.0 on 2022-06-06 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('knowledge', '0008_tag_skill_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
