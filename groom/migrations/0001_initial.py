# Generated by Django 5.1.2 on 2024-11-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='gifts')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('significance', models.IntegerField()),
                ('reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
