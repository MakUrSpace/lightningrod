from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='lightningrod',
    version='0.0.1',
    author='MakUrSpace',
    author_email='hello@makurspace.com',
    description='MakerModule Automation Interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.makurspace.com',
    packages=["lightningrod"],
    install_requires=["justpy", "groundplane"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ShareAlike v3.0",
        "Operating System :: OS Independent",
    ),
)
