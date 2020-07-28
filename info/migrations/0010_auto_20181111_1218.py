from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20181111_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('7:30 - 8:30', '7:30 - 8:30'), ('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], default='11:00 - 11:50', max_length=50),
        ),
    ]
