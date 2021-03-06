#-
# Copyright (c) 2012 Ben Thorner
# Copyright (c) 2013 Colin Rothwell
# All rights reserved.
#
# This software was developed by Ben Thorner as part of his summer internship
# and Colin Rothwell as part of his final year undergraduate project.
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
from nose.plugins.attrib import attr

class test_raw_fpu_cun(BaseBERITestCase):
    def test_cun_single(self):
        '''Test we can compare unordered in single precision'''
        self.assertRegisterEqual(self.MIPS.s0, 0x1, "Failed to compare unordered QNaN, QNaN in single precision")
        self.assertRegisterEqual(self.MIPS.s3, 0x0, "Failed to compare unordered 2.0, 2.0 in single precision")

    @attr('float64')
    def test_cun_double(self):
        '''Test we can compare unordered in double precision'''
        self.assertRegisterEqual(self.MIPS.s1, 0x1, "Failed to compare unordered QNaN, QNaN in double precision")
        self.assertRegisterEqual(self.MIPS.s4, 0x0, "Failed to compare unordered 1.0, 1.0 in double precision")

    @attr('floatpaired')
    def test_cun_paired(self):
        '''Test we can compare unordered paired singles'''
        self.assertRegisterEqual(self.MIPS.s2, 0x1, "Failed to compare unordered 0, QNaN and 0, QNaN in paired single precision")
        self.assertRegisterEqual(self.MIPS.s5, 0x0, "Failed to compare unordered 2.0, 1.0 and 1.0, 2.0 in paired single precision")
