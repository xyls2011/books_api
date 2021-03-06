# Generated by Django 2.1.4 on 2019-01-04 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.CharField(max_length=100)),
                ('capterid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserReadStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_status', models.CharField(blank=True, max_length=100)),
                ('word_size', models.CharField(blank=True, max_length=100)),
                ('bg_color', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(blank=True, max_length=100)),
                ('session_key', models.CharField(blank=True, max_length=100)),
                ('code', models.CharField(blank=True, max_length=100)),
                ('book', models.ManyToManyField(blank=True, to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='userreadstatus',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
        migrations.AddField(
            model_name='bookcapter',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]
