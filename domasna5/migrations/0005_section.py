# Generated by Django 4.0.4 on 2022-07-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domasna5', '0004_quiz_courseuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]