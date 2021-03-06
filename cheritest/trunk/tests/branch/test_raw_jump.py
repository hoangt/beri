#-
# Copyright (c) 2011 Steven J. Murdoch
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

class test_raw_jump(BaseBERITestCase):
    def test_j_before(self):
        self.assertRegisterEqual(self.MIPS.a0, 1, "instruction before j missed")

    def test_j_branch_delay(self):
        self.assertRegisterEqual(self.MIPS.a2, 2, "instruction in branch-delay slot missed")

    def test_j_skipped(self):
        self.assertRegisterNotEqual(self.MIPS.a3, 3, "jump didn't happen")

    def test_j_target(self):
        self.assertRegisterEqual(self.MIPS.a4, 4, "instruction at jump target didn't run")
