# Generated by Django 4.0.4 on 2022-07-26 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domasna5', '0014_remove_quizprofile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correctAnswer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domasna5.question'),
        ),
    ]