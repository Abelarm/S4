from distutils.core import setup, Extension

libs = ['S4', 'stdc++', 'gfortran']
libs.extend( [lib[2::] for lib in '     '.split()])

S4module = Extension('S4',
	sources = [
		'S4/main_python.c'
	],
	libraries = libs,
	library_dirs = ['build'],
	extra_link_args = [
		'build/libS4.a'
	]
)

setup(name = 'S4',
	version = '1.1',
	description = 'Stanford Stratified Structure Solver (S4): Fourier Modal Method',
	ext_modules = [S4module]
)
