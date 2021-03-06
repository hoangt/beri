#-
# Copyright (c) 2012 Michael Roe
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
from nose.plugins.attrib import attr

#
# Test that clc raises an exception if it does not have Permit_Load_Capability
# permission.
#

class test_cp2_x_clc_perm(BaseBERITestCase):
    @attr('capabilities')
    def test_cp2_x_clc_perm_1(self):
        '''Test clc did not load a capability without Permit_Load_Capability'''
        self.assertRegisterEqual(self.MIPS.a0, 0,
            "clc read a capability without Permit_Load_Capability permission")

    @attr('capabilities')
    def test_cp2_x_clc_perm_2(self):
        '''Test clc raises an exception when it does not have Permit_Load_Capability permission'''
        self.assertRegisterEqual(self.MIPS.a2, 1,
            "clc did not raise an exception when it did not have Permit_Load_Capability permission")
    @attr('capabilities')

    def test_cp2_x_clc_perm_3(self):
        '''Test capability cause was set correctly when didn't have Permit_Load_Capability permission'''
        self.assertRegisterEqual(self.MIPS.a3, 0x1402,
            "Capability cause was not set correctly when didn't have Permit_Load_Capability permission")
