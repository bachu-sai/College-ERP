from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20181109_2013'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assigntime',
            unique_together={('assign', 'period', 'day')},
        ),
    ]
