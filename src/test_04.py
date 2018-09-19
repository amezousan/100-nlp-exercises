#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import importlib
import os

script_name = os.path.basename(__file__)[5:-3]
module      = importlib.import_module("code." + script_name)

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("\n# In method", self._testMethodName, ":")

    def test_output(self):
        self.assertEqual(u"1:H, 2:He, 3:Li, 4:Be, 5:B, 6:C, 7:N, 8:O, 9:F, 10:Ne, 11:Na, 12:Mi, 13:Al, 14:Si, 15:P, 16:S, 17:Cl, 18:Ar, 19:K, 20:Ca", module.output(u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))

    def test_anotherword_for_onechar_output(self):
        self.assertEqual(u"1:I, 2:He, 3:Li, 4:Be, 5:O, 6:O, 7:O, 8:X, 9:L, 10:Ne, 11:Na, 12:Mi, 13:Al, 14:Si, 15:E, 16:E, 17:Cl, 18:Ar, 19:I, 20:Ca", module.output(u"Ii He Lied Because Ooron Oould Oot Xxidize Lluorine. New Nations Might Also Sign Eeace Eecurity Clause. Arthur Iing Can."))

    def test_anotherword_for_twochars_output(self):
        self.assertEqual(u"1:H, 2:Ee, 3:Ii, 4:Ee, 5:B, 6:C, 7:N, 8:O, 9:F, 10:Ee, 11:Aa, 12:Ii, 13:Ll, 14:Ii, 15:P, 16:S, 17:Ll, 18:Rr, 19:K, 20:Aa", module.output(u"Hi Ee Iied Eecause Boron Could Not Oxidize Fluorine. Eew Aations Iight Llso Iign Peace Security Llause. Rrthur King Aan."))

if __name__ == "__main__":
    unittest.main()