from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20181109_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(default='1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='assign',
            unique_together={('course', 'class_id', 'teacher')},
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together={('studentcourse', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='marksclass',
            unique_together={('assign', 'name')},
        ),
    ]
