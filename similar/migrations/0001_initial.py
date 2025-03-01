# Generated by Django 4.2.11 on 2025-02-28 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_question', models.CharField(max_length=60)),
                ('name_question_user', models.CharField(max_length=20)),
                ('pub_date', models.DateField(verbose_name='Publié le')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_answer', models.CharField(max_length=60)),
                ('name_question_user', models.CharField(max_length=20)),
                ('pub_date', models.DateField(verbose_name='Publié le')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='similar.questions')),
            ],
        ),
    ]
