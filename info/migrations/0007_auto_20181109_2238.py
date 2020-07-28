from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
