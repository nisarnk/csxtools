from setuptools import setup, Extension
import numpy

ext_modules = [
    Extension(
        'csxtools.ext.fastccd',
        sources=["src/fastccdmodule.c", "src/fastccd.c"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-lgomp"],
        include_dirs=[numpy.get_include()]
    ),
    Extension(
        'csxtools.ext.axis1',
        sources=["src/axis1module.c", "src/axis1.c"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-lgomp"],
        include_dirs=[numpy.get_include()]
    ),
    Extension(
        'csxtools.ext.image',
        sources=["src/imagemodule.c", "src/image.c"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-lgomp"],
        include_dirs=[numpy.get_include()]
    ),
    Extension(
        'csxtools.ext.phocount',
        sources=["src/phocountmodule.c", "src/phocount.c"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-lgomp"],
        include_dirs=[numpy.get_include()]
    ),
]

setup(
    ext_modules=ext_modules,
)
