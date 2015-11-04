#!/usr/bin/env Python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import agate

class AgateTestCase(unittest.TestCase):
    def assertColumnNames(self, table, names):
        self.assertIsInstance(table, agate.Table)

        self.assertSequenceEqual(table.column_names, names)
        self.assertSequenceEqual(
            [c.name for c in table.columns],
            names
        )

    def assertColumnTypes(self, table, types):
        self.assertIsInstance(table, agate.Table)

        table_types = table.column_types
        column_types = [c.data_type for c in table.columns]

        for i, test_type in enumerate(types):
            self.assertIsInstance(table_types[i], test_type)
            self.assertIsInstance(column_types[i], test_type)

    def assertRows(self, table, rows):
        self.assertIsInstance(table, agate.Table)

        for i, row in enumerate(rows):
            self.assertSequenceEqual(table.rows[i], row)

    def assertRowNames(self, table, names):
        self.assertIsInstance(table, agate.Table)

        self.assertSequenceEqual(table.row_names, names)
        self.assertSequenceEqual(
            table.rows.keys(),
            names
        )