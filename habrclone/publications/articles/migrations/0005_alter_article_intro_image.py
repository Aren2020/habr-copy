# Generated by Django 5.0.6 on 2024-08-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='intro_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
