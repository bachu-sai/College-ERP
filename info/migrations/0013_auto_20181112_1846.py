from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20181111_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.Dept'),
        ),
    ]
