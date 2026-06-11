import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groom', '0003_gifts_reserved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gifts',
            name='reserved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groom.guests'),
        ),
        migrations.AlterField(
            model_name='guests',
            name='token',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
