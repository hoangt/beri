/*-
 * Copyright (c) 2013 Colin Rothwell
 * All rights reserved.
 *
 * This software was developed by Colin Rothwell as part of his final year
 * undergraduate project.
 *
 * @BERI_LICENSE_HEADER_START@
 *
 * Licensed to BERI Open Systems C.I.C. (BERI) under one or more contributor
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
import CoProFPTypes::*;

import "BVI" doubleAddWrapper =
module mkVerilogDoubleAddMegafunction(VerilogDiadicDoubleMegafunction);
    default_clock clk;
    default_reset no_reset;

    input_clock clk (clock) <- exposeCurrentClock;

    method place(dataa, datab) enable (dummy_enable);
    method result result();

    schedule (place, result) CF (place, result);
endmodule

import "BVI" floatAddWrapper =
module mkVerilogFloatAddMegafunction(VerilogDiadicFloatMegafunction);
    default_clock clk;
    default_reset no_reset;

    input_clock clk (clock) <- exposeCurrentClock;

    method place(dataa, datab) enable (dummy_enable);
    method result result();

    schedule (place, result) CF (place, result);
endmodule

import "BVI" doubleMulWrapper =
module mkVerilogDoubleMulMegafunction(VerilogDiadicDoubleMegafunction);
    default_clock clk;
    default_reset no_reset;

    input_clock clk (clock) <- exposeCurrentClock;

    method place(dataa, datab) enable (dummy_enable);
    method result result();

    schedule (place, result) CF (place, result);
endmodule

import "BVI" floatMulWrapper =
module mkVerilogFloatMulMegafunction(VerilogDiadicFloatMegafunction);
    default_clock clk;
    default_reset no_reset;

    input_clock clk (clock) <- exposeCurrentClock;

    method place(dataa, datab) enable (dummy_enable);
    method result result();

    schedule (place, result) CF (place, result);
endmodule

import "BVI" doubleDivWrapper =
module mkVerilogDoubleDivMegafunction(VerilogDiadicDoubleMegafunction);
    default_clock clk;
    default_reset no_reset;

    input_clock clk (clock) <- exposeCurrentClock;

    method place(dataa, datab) enable (dummy_enable);
    method result result();

    schedule (place, result) CF (place, result);
endmodule
