from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20181111_1218'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assigntime',
            unique_together=set(),
        ),
    ]
