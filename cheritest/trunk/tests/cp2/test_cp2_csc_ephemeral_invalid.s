#-
# Copyright (c) 2012-2014 Michael Roe
# Copyright (c) 2012-2014 Robert M. Norton
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
# Test that csc does NOT raise an exception when storing an invalid, ephemeral
# capability via a capability with the store ephemeral bit unset.
#

		.global test
test:		.ent test
		daddu 	$sp, $sp, -32
		sd	$ra, 24($sp)
		sd	$fp, 16($sp)
		daddu	$fp, $sp, 32

		#
		# Set up exception handler
		#

		jal	bev_clear
		nop
		dla	$a0, bev0_handler
		jal	bev0_handler_install
		nop

		# $a2 will be set to 1 if the exception handler is called
		dli	$a2, 0

		#
		# Make $c1 an ephemeral capability. It is ephemeral,
		# but untagged so storing it should be allowed
		#

		dli       $t0, 0x7e
		candperm  $c1, $c1, $t0
		ccleartag $c1, $c1

		#
		# Remove Permit_Store_Ephemeral from $c2
		#
		
		dli $t0, 0xbf
		candperm $c2, $c0, $t0

		# Try to store the ephemeral capability via a capbility
		# that doesn't permit this.

		dla     $t0, cap1
		cscr    $c1, $t0($c2) # This should not raise an exception

		# Check that the store did happen.
		cldr    $s0, $t0($c0)
		daddiu  $t0, $t0, 8
		cldr    $s1, $t0($c0)
		daddiu  $t0, $t0, 8
		cldr    $s2, $t0($c0)
		daddiu  $t0, $t0, 8
		cldr    $s3, $t0($c0)

		ld	$fp, 16($sp)
		ld	$ra, 24($sp)
		daddu	$sp, $sp, 32
		jr	$ra
		nop			# branch-delay slot
		.end	test

		.ent bev0_handler
bev0_handler:
		li	$a2, 1
		cgetcause $a3
		dmfc0	$a5, $14	# EPC
		daddiu	$k0, $a5, 4	# EPC += 4 to bump PC forward on ERET
		dmtc0	$k0, $14
		nop
		nop
		nop
		nop
		eret
		.end bev0_handler

		.data
		.align	3
data:		.dword	0x0123456789abcdef
		.dword  0x0123456789abcdef

		.align 5
cap1:		.dword 0x0123456789abcdef
		.dword 0x0123456789abcdef
		.dword 0x0123456789abcdef
		.dword 0x0123456789abcdef
