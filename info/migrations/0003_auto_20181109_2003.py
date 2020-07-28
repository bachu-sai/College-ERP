from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20181109_1947'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentcourse',
            unique_together={('student', 'course')},
        ),
    ]
