# Generated by Django 3.1.4 on 2021-01-06 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0014_auto_20210106_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='minut',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='url',
            name='sec',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ResultUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('h1', models.CharField(max_length=255)),
                ('encoding', models.CharField(max_length=100)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.url')),
            ],
        ),
    ]
