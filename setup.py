from setuptools import setup, find_packages

setup(
    name='overallsystemdata',
    packages=find_packages(),
    version='1.0',
    author='Aliaksandr Shamchonak',
    author_email='Aliaksandr_Shamchonak@epam.com',
    description='Gets common system information '
                'every given time interval and writes to the txt|json file',
    license="MIT",
    install_requires=[
        'psutil'
    ],
    include_package_data=True
)
