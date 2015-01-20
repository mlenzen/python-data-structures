#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from invoke import run, task
from invoke.util import log


@task
def clean():
	"""clean - remove build artifacts."""
	run('rm -rf build/')
	run('rm -rf dist/')
	run('rm -rf data_structures.egg-info')
	run('find . -name *.pyc -delete')
	run('find . -name *.pyo -delete')
	run('find . -name *~ -delete')
	run('find . -name __pycache__ -delete')

	log.info('cleaned up')


@task(clean)
def publish():
	"""publish - package and upload a release to the cheeseshop."""
	run('python setup.py sdist upload', pty=True)
	run('python setup.py bdist_wheel upload', pty=True)

	log.info('published new release')
