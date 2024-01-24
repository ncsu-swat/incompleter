# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54114678/how-to-fix-argument-must-be-a-string-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import migrations, models
    _l_(656665)

except ImportError:
    pass
try:
    import django.db.models.deletion
    _l_(656667)

except ImportError:
    pass


class Migration(_a_(656669, _n_(656668, "migrations", lambda: migrations), "Migration")):
    _l_(656738)


    initial = True
    _l_(656670)

    dependencies = [
    ]
    _l_(656671)

    operations = [
        _c_(656683, _a_(656673, _n_(656672, "migrations", lambda: migrations), "CreateModel"), name='DepartmentData',
            fields=[
                ('id', _c_(656676, _a_(656675, _n_(656674, "models", lambda: models), "AutoField"), auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', _c_(656679, _a_(656678, _n_(656677, "models", lambda: models), "CharField"), max_length=50)),
                ('created_on', _c_(656682, _a_(656681, _n_(656680, "models", lambda: models), "DateTimeField"), auto_now_add=True)),
            ],
        ),
        _c_(656695, _a_(656685, _n_(656684, "migrations", lambda: migrations), "CreateModel"), name='FacultyData',
            fields=[
                ('id', _c_(656688, _a_(656687, _n_(656686, "models", lambda: models), "AutoField"), auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', _c_(656691, _a_(656690, _n_(656689, "models", lambda: models), "CharField"), max_length=30)),
                ('created_on', _c_(656694, _a_(656693, _n_(656692, "models", lambda: models), "DateTimeField"), auto_now_add=True)),
            ],
        ),
        _c_(656707, _a_(656697, _n_(656696, "migrations", lambda: migrations), "CreateModel"), name='SemesterData',
            fields=[
                ('id', _c_(656700, _a_(656699, _n_(656698, "models", lambda: models), "AutoField"), auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', _c_(656703, _a_(656702, _n_(656701, "models", lambda: models), "CharField"), max_length=50)),
                ('status', _c_(656706, _a_(656705, _n_(656704, "models", lambda: models), "IntegerField"), choices=[('0', 'Yes'), ('1', 'No')], default=('1', 'No'))),
            ],
        ),
        _c_(656716, _a_(656709, _n_(656708, "migrations", lambda: migrations), "CreateModel"), name='SessionData',
            fields=[
                ('id', _c_(656712, _a_(656711, _n_(656710, "models", lambda: models), "AutoField"), auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', _c_(656715, _a_(656714, _n_(656713, "models", lambda: models), "CharField"), max_length=15)),
            ],
        ),
        _c_(656726, _a_(656718, _n_(656717, "migrations", lambda: migrations), "AddField"), model_name='semesterdata',
            name='sid',
            field=_c_(656725, _a_(656720, _n_(656719, "models", lambda: models), "ForeignKey"), on_delete=_a_(656724, _a_(656723, _a_(656722, _a_(656721, django, "db"), "models"), "deletion"), "CASCADE"), to='system.SessionData'),
        ),
        _c_(656736, _a_(656728, _n_(656727, "migrations", lambda: migrations), "AddField"), model_name='departmentdata',
            name='fid',
            field=_c_(656735, _a_(656730, _n_(656729, "models", lambda: models), "ForeignKey"), on_delete=_a_(656734, _a_(656733, _a_(656732, _a_(656731, django, "db"), "models"), "deletion"), "CASCADE"), to='system.FacultyData'),
        ),
    ]
    _l_(656737)