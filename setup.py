from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='tensor2robot',
    version='0.1.0',
    packages=['tensor2robot'],
    license="MIT",
    long_description=long_description,
    install_requires=['wheel',
                      'absl-py>=0.5.0',
                      'numpy>=1.13.3',
                      'tensorflow>=1.13.0',
                      'tensorflow-serving-api>=1.13.0',
                      'gin-config>=0.1.4',
                      'pybullet==2.5.0',
                      'Pillow==5.3.0',
                      'gym>=0.10.9',
                      'tensorflow-probability>=0.6.0',
                      'tf-slim>=1.0'
                      ]
)
