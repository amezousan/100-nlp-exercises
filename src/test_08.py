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

    # Normal cases
    def test_encrypt_with_cipher_case1(self):
        input_message  = "heLlo"
        expect_message = "svLol"
        self.assertEqual(expect_message, module.cipher(input_message))

    def test_encrypt_with_cipher_case2(self):
        input_message  = u"heLlo2ユー!"
        expect_message = u"svLol2ユー!"
        self.assertEqual(expect_message, module.cipher(input_message))

    def test_decrypt_with_cipher_case1(self):
        input_message   = u"svLol2ユー!"
        expect_message  = u"heLlo2ユー!"
        self.assertEqual(expect_message, module.cipher(input_message))

if __name__ == "__main__":
    unittest.main()