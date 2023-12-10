# Generated by Django 4.2.5 on 2023-11-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0006_remove_lab_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='name',
            field=models.CharField(help_text='Введите название лабы', max_length=20, null=True, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='Extra_Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название факутальтива', max_length=20, null=True, verbose_name='Title')),
                ('student', models.ManyToManyField(to='test_django.student')),
                ('tutor', models.ManyToManyField(to='test_django.tutor')),
            ],
            options={
                'db_table': 'Extra_Lessons',
            },
        ),
    ]
