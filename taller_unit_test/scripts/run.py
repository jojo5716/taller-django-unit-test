# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys

from django.core.management import execute_from_command_line

parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_path)
# if we activate virtualenv within npm command we need to go up one more
# directory
sys.path.insert(0, os.path.dirname(parent_path))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

if __name__ == "__main__":
    args = sys.argv
    args.insert(1, "test")
    execute_from_command_line(args)
