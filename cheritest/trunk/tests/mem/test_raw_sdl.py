#-
# Copyright (c) 2011 William M. Morland
# All rights reserved.
#
# This software was developed by SRI International and the University of
# Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-10-C-0237
# ("CTSRD"), as part of the DARPA CRASH research programme.
#
# @BERI_LICENSE_HEADER_START@
#
# Licensed to BERI Open Systems C.I.C. (BERI) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  BERI licenses this
# file to you under the BERI Hardware-Software License, Version 1.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#   http://www.beri-open-systems.org/legal/license-1-0.txt
#
# Unless required by applicable law or agreed to in writing, Work distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
# @BERI_LICENSE_HEADER_END@
#

from beritest_tools import BaseBERITestCase

class test_raw_sdl(BaseBERITestCase):
	def test_a1(self):
		self.assertRegisterEqual(self.MIPS.a1, 0xfedcba9876543210, "SDL with zero offset failed")

	def test_a2(self):
		self.assertRegisterEqual(self.MIPS.a2, 0xfefedcba98765432, "SDL with one byte offset failed")

	def test_a3(self):
		self.assertRegisterEqual(self.MIPS.a3, 0xfefefedcba987654, "SDL with two byte offset failed")

	def test_a4(self):
		self.assertRegisterEqual(self.MIPS.a4, 0xfefefefedcba9876, "SDL with three byte offset failed")

	def test_a5(self):
		self.assertRegisterEqual(self.MIPS.a5, 0xfefefefefedcba98, "SDL with four byte offset failed")

	def test_a6(self):
		self.assertRegisterEqual(self.MIPS.a6, 0xfefefefefefedcba, "SDL with five byte offset failed")

	def test_a7(self):
		self.assertRegisterEqual(self.MIPS.a7, 0xfefefefefefefedc, "SDL with six byte offset failed")

	def test_t0(self):
		self.assertRegisterEqual(self.MIPS.t0, 0xfefefefefefefefe, "SDL with seven byte offset failed")

	def test_t1(self):
		self.assertRegisterEqual(self.MIPS.t1, 0xfedcba9876543210, "SDL with full doubleword offset failed")
