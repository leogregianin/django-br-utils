import glob
import os
import os.path
import sys
from invoke import task


@task
def clean(c):
    c.run('git clean -Xfd')


@task
def test(c, country='all'):
    print('Python version: ' + sys.version)
    test_cmd = 'coverage run `which django-admin` test --settings=tests.settings'
    country = os.environ.get('COUNTRY', country)

    # Fix issue #49
    cwp = os.path.dirname(os.path.abspath(__name__))
    pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)
    pythonpath.append(os.path.join(cwp, 'tests'))
    os.environ['PYTHONPATH'] = os.pathsep.join(pythonpath)

    c.run('{0} tests'.format(test_cmd))
    c.run('coverage report')

@task
def prospector(c):
    c.run('prospector --profile .prospector.yaml br_utils')
