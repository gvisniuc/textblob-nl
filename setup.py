import sys
import subprocess
import re
from setuptools import setup

packages = ['textblob_nl']
requires = ["textblob>=0.8.0"]

PUBLISH_CMD = "python setup.py register sdist bdist_wheel upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist bdist_wheel upload -r test'
TEST_CMD = 'python run_tests.py'


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("textblob_nl/__init__.py")

if 'publish' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()

if 'run_tests' in sys.argv:
    try:
        __import__('nose')
    except ImportError:
        print('nose required. Run `pip install nose`.')
        sys.exit(1)

    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='textblob-nl',
    version=__version__,
    description='Dutch language support for TextBlob.',
    long_description_content_type='text/x-rst',
    long_description=(read("README.rst") + '\n\n' +
                        read("HISTORY.rst")),
    author='George Visniuc',
    author_email='georgevisniuc@gmail.com',
    url='https://github.com/gvisniuc/textblob-nl',
    packages=packages,
    package_dir={'textblob_nl': 'textblob_nl'},
    include_package_data=True,
    package_data={
        "textblob_nl": ["*.txt", "*.xml"]
    },
    install_requires=requires,
    license=read("LICENSE"),
    zip_safe=False,
    keywords=[
        'textblob',
        'textblob_nl',
        'nlp',
        'linguistics',
        'nltk',
        'pattern'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=['nose'],
)
