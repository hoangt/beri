#-
# Copyright (c) 2013 Michael Roe
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

#
# Test that an exception in the integer pipeline (syscall) cancels a
# instruction in progress in the FPU.
#

from beritest_tools import BaseBERITestCase
from nose.plugins.attrib import attr

class test_fpu_exception_pipeline(BaseBERITestCase):

    def test_fpu_exception_pipeline_1(self):
        '''Test mtc1 was cancelled by exception'''
	self.assertRegisterEqual(self.MIPS.a0, 0x3f800000, "mtc1 was not cancelled by exception")

    def test_fpu_exception_pipeline_2(self):
        '''Test add.s was cancelled by exception'''
	self.assertRegisterEqual(self.MIPS.a1, 0, "add.s was not cancelled by exception")
