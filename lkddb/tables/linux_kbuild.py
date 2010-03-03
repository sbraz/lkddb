#: lkddb/linux/version.py : sources reader for Linux kernels
#
#  Copyright (c) 2000,2001,2007-2009  Giacomo A. Catenazzi <cate@cateee.net>
#  This is free software, see GNU General Public License v2 for details

import lkddb
from lkddb import fmt

class kver_table(lkddb.table):

    def __init__(self, tree):
        lkddb.table.__init__(self, "kver", tree)

    cols = (('version', fmt.m32x, "INTEGER"),
           ('ver_str', fmt.str, "TEXT"),
           ('is_a_release', fmt.int, "INTEGER"),
           ('name', fmt.qstr, "TEXT"))


class kconf_table(lkddb.table):

    def __init__(self, tree):
        lkddb.table.__init__(self, "kconf", tree)

    cols = (('config', None, "TEXT"),
           ('filename', None, "TEXT"),
           ('type', None, "TEXT"),
           ('descr', None, "TEXT"),
           ('depends', None, "TEXT"),
           ('help', None, "TEXT"))

    def add_row_fmt(self, row):
	pass

    def get_lines(self):
        # we don't export lines for kconf: multiline data
        return []


class module_table(lkddb.table):

    def __init__(self, tree):
        lkddb.table.__init__(self, "module", tree)

    cols = (('name', fmt.str, "TEXT"),
           ('descr', fmt.qstr, "TEXT"),
           ('config',  fmt.str, "$config"),
           ('filename', fmt.filename, "$filename"))


class firmware_table(lkddb.table):

    def __init__(self, tree):
        lkddb.table.__init__(self, "firmware", tree)

    cols = (('config',  fmt.str, "$config"),
           ('filename', fmt.filename, "$filename"))
