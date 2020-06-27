# Generated by Django 3.0.7 on 2020-06-27 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mySchool', '0002_student_trafees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Class',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.CreateModel(
            name='StudentFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mySchool.Student')),
            ],
        ),
    ]
