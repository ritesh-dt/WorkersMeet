# Generated by Django 3.0.7 on 2020-11-16 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
        ('jobsapp', '0010_auto_20201107_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicant',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('soft_deleted', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us', to='jobsapp.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
