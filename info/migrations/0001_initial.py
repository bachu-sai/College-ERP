from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AssignTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('7:30 - 8:30', '7:30 - 8:30'), ('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], default='8:30 - 9:30', max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=15)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Assign')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2018-10-23')),
                ('status', models.BooleanField(default='True')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(default=0)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Assign')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('section', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(default='X', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50)),
                ('marks1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='MarksClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50)),
                ('status', models.BooleanField(default='False')),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Assign')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('USN', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('class_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.Class')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Dept')),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='studentcourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.StudentCourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Dept'),
        ),
        migrations.AddField(
            model_name='class',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Dept'),
        ),
        migrations.AddField(
            model_name='attendancetotal',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Course'),
        ),
        migrations.AddField(
            model_name='attendancetotal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendanceclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.AttendanceClass'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Course'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Student'),
        ),
        migrations.AddField(
            model_name='assign',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Class'),
        ),
        migrations.AddField(
            model_name='assign',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Course'),
        ),
        migrations.AddField(
            model_name='assign',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Teacher'),
        ),
    ]
