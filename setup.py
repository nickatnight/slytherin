from setuptools import setup

APP = ['slytherin.py']
DATA_FILES = [('', ['images'])]
OPTIONS = {
    'iconfile': 'snakei.icns',
    'includes': ['menu.py'],
}

setup(
    app=APP,
    name='Snake',
    version="1.0.1",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
