__version__ = "0.0.3"

from glob import glob
from setuptools import setup
try:
    from pybind11.setup_helpers import Pybind11Extension
except ImportError:
    from setuptools import Extension as Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "WhileDB._WhileDB",
        sorted(glob("src/*.cpp")),
    ),
]

setup(
    name="WhileDB",
    version=__version__,
    author="HellOwhatAs",
    url="https://github.com/HellOwhatAs/While-DB",
    description="WhileDB language intepreter intrduced on SJTU CS2612.",
    ext_modules=ext_modules,
    packages=['WhileDB'],
    package_data = {
        'WhileDB': ['*.pyi'],
    },
    setup_requires=["pybind11"],
    zip_safe=False,
)