# Generated by Django 4.1.5 on 2023-02-12 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book'),
        ),
    ]