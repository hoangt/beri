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

.set mips64
.set noreorder
.set nobopt
.set noat

#
# Test conversion from 64-bit int to single-precision floating point when
# the FPU is in 64-bit mode
#
		.text
		.global start
		.ent start
start:     
		mfc0 $t0, $12
		li $t1, 1 << 29		# Enable CP1
		or $t0, $t0, $t1    
		li $t1, 1 << 26		# Put FPU into 64 bit mode
		or $t0, $t0, $t1
		mtc0 $t0, $12 
		nop
		nop
		nop

		dli $t0, 0
		dmtc1 $t0, $f2
		cvt.s.l $f2, $f2
		dmfc1 $a0, $f2

		dli $t0, 1
		dmtc1 $t0, $f2
		cvt.s.l $f2, $f2
		dmfc1 $a1, $f2

		dli $t0, 1
		dsll $t0, $t0, 32
		ori $t0, $t0, 1
		dmtc1 $t0, $f2
		cvt.s.l $f2, $f2
		dmfc1 $a2, $f2

		# Dump registers on the simulator (gxemul dumps regs on exit)
		mtc0 $at, $26
		nop
		nop

		# Terminate the simulator
		mtc0 $at, $23
end:
		b end
		nop

.end start
