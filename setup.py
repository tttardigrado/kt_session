from setuptools import setup
setup(
    name='kt',
    version='0.1.0',
    packages=['kt'],
    entry_points={
        'console_scripts': [
            'kt = kt.__main__:main'
        ]
    })
