import codecs
import setuptools
import setuptools.command.test
import sys


def long_description():
    try:
        return codecs.open('README.rst', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


def _strip_comments(l):
    return l.split('#', 1)[0].strip()


def install_requires():
    return [_strip_comments(req) for req in codecs.open('requirements.txt', 'r', 'utf-8').readlines() if req]


def tests_require():
    return [_strip_comments(req) for req in codecs.open('requirements_test.txt', 'r', 'utf-8').readlines() if req]


class nosetest(setuptools.command.test.test):
    def initialize_options(self):
        setuptools.command.test.test.initialize_options(self)
        self.argv = [
            '--cover-branches', '--with-coverage', '--cover-erase', '--cover-package=celery_pubsub', 'tests/pubsub.py'
        ]

    def run_tests(self):
        import nose
        sys.exit(nose.main(argv=self.argv))


setuptools.setup(
    name='celery-pubsub',
    packages=['celery_pubsub'],
    version='0.1.6',
    description='A Publish and Subscribe library for Celery',
    long_description=long_description(),
    author='Samuel GIFFARD',
    author_email='mulugruntz@gmail.com',
    license='MIT',
    url='https://github.com/Mulugruntz/celery-pubsub',
    download_url='https://github.com/Mulugruntz/celery-pubsub/tarball/0.1.6',
    keywords=['celery', 'publish', 'subscribe', 'pubsub'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
    ],
    cmdclass={'test': nosetest},
    install_requires=install_requires(),
    tests_require=tests_require(),
)
