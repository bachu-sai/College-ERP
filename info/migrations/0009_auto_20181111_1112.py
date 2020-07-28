from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20181111_1107'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendancetotal',
            unique_together={('student', 'course')},
        ),
    ]
