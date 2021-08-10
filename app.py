#!/usr/bin/env python
# Encoding: utf-8
#  _____.__           .
# /  _____/           |\
# | |_|_|.__ _._  ..  | |.  ._ .____
# |  __/|/ _` | \ /\ /| | | | / ___/
# | | | | (.] |\ V  V | | \.| \___ \
# | | | |\__,_/.\_/\_/| |\__  [____/
# |/   \|             |/ \___/
#       '             '
__author__ = 'Jacob Betz'
__email__ = 'jake@baruek.net'


from app import create_app


flawlys = create_app(debug=True)
