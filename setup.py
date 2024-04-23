from setuptools import setup, find_packages

setup(
    name='stremaz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'requests'
    ],
    
    entry_points={
        'console_scripts': [
            'stremaz = app.main:app'
        ]
    }
    
)
# Path: app/settings/config.py

