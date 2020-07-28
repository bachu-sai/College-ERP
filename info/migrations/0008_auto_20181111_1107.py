from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20181109_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentcourse',
            options={'verbose_name_plural': 'Marks'},
        ),
    ]
