from setuptools import setup


setup(
    name="WhileDB",
    python_requires='==3.8.*',
    description="WhileDB language intepreter intrduced on SJTU CS2612.",
    url="https://github.com/HellOwhatAs/While-DB",
    version="0.0.2",
    packages=['WhileDB'],
    author="HellOwhatAs",
    license="MIT",
    include_package_data=True,
    platforms=['windows'],
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
    ],
)