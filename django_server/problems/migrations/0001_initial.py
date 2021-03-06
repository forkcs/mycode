# Generated by Django 3.1.2 on 2020-10-31 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100000)),
                ('language', models.SmallIntegerField(choices=[(1, 'Python'), (2, 'C++')])),
                ('tests', models.CharField(max_length=1000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name': 'Problem',
                'verbose_name_plural': 'Problems',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100000)),
                ('status', models.SmallIntegerField(blank=True, choices=[(1, 'OK'), (2, 'Error'), (3, 'Pending'), (4, 'No Status')], default=4, null=True)),
                ('score', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name': 'Solution',
                'verbose_name_plural': 'Solutions',
            },
        ),
    ]
