from setuptools import setup, find_packages

setup(
    name="todobackend",
    version="0.1.0",
    description="todobackend django rest service",
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],
    install_requires=[
        "awscli == 1.15.7",
        "boto == 2.48.0",
        "boto3 == 1.7.7",
        "botocore == 1.10.7",
        "Django >= 1.11.12,<2.0",
        "django-cors-headers == 2.2.0",
        "djangorestframework == 3.8.2",
        "docutils == 0.14",
        "futures == 3.2.0",
        "jmespath == 0.9.3",
        "MySQL-python == 1.2.5",
        "pyasn1 == 0.4.2",
        "python-dateutil == 2.7.2",
        "pytz == 2018.4",
        "PyYAML == 3.12",
        "rsa == 3.4.2",
        "s3transfer == 0.1.13",
        "six == 1.11.0",
        "uwsgi>=2.0",
    ],
    extras_require={
        "test": [
            "colorama == 0.3.7",
            "coverage == 4.5.1",
            "django-nose == 1.4.5",
            "nose == 1.3.7",
            "pinocchio == 0.4.2",
        ]
    }
)
