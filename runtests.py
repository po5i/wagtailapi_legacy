#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals

import argparse
import os
import shutil
import sys
import warnings

from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--deprecation', choices=['all', 'pending', 'imminent', 'none'], default='imminent')
    parser.add_argument('--postgres', action='store_true')
    return parser


def parse_args(args=None):
    return make_parser().parse_known_args(args)


def runtests():
    args, rest = parse_args()

    if args.postgres:
        os.environ['DATABASE_ENGINE'] = 'django.db.backends.postgresql'

    execute_from_command_line([sys.argv[0], 'test'] + rest)

if __name__ == '__main__':
    runtests()
