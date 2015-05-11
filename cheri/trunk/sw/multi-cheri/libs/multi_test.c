/*-
 * Copyright (c) 2014 Alexandre Joannou
 * All rights reserved.
 *
 * This software was developed by SRI International and the University of
 * Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-10-C-0237
 * ("CTSRD"), as part of the DARPA CRASH research programme.
 *
 * This software was developed by SRI International and the University of
 * Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249
 * ("MRC2"), as part of the DARPA MRC research programme.
 *
 * @BERI_LICENSE_HEADER_START@
 *
 * Licensed to BERI Open Systems C.I.C (BERI) under one or more contributor
 * license agreements.  See the NOTICE file distributed with this work for
 * additional information regarding copyright ownership.  BERI licenses this
 * file to you under the BERI Hardware-Software License, Version 1.0 (the
 * "License"); you may not use this file except in compliance with the
 * License.  You may obtain a copy of the License at:
 *
 *   http://www.beri-open-systems.org/legal/license-1-0.txt
 *
 * Unless required by applicable law or agreed to in writing, Work distributed
 * under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations under the License.
 *
 * @BERI_LICENSE_HEADER_END@
 */

#include "multi_test.h"
#include "uart.h"

void test_default ()
{
    asm volatile ("nop": : );
}

void test_print ()
{
    uart_puts(" __test_print__ \n");
}

void test_print_locked ()
{
    uart_locked_puts(" __test_print_locked__ \n");
}

void multi_default_init (test_function_t * mtest)
{
    int i;
    for (i = 0; i < MAX_CORE; i++)
        mtest[i] = &test_default;
}

void multi_print_init (test_function_t * mtest)
{
    int i;
    for (i = 0; i < MAX_CORE; i++)
        mtest[i] = &test_print;
}

void multi_print_locked_init (test_function_t * mtest)
{
    int i;
    uart_lock_init();
    for (i = 0; i < MAX_CORE; i++)
        mtest[i] = &test_print_locked;
}