#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr
from scipy import linalg 

class Algorithm2(gr.sync_block):
    """
    docstring for block Algorithm2
    """
    def __init__(self, Xtx1, Ytx1, Xtx2, Ytx2, Xtx3, Ytx3, Xtx4, Ytx4):
	self.Xtx1 = Xtx1
	self.Ytx1 = Ytx1
	self.Xtx2 = Xtx2
	self.Ytx2 = Ytx2
	self.Xtx3 = Xtx3
	self.Ytx3 = Ytx3
	self.Xtx4 = Xtx4
	self.Ytx4 = Ytx4
	self.B_0_0 = np.square(Xtx1)-np.square(Xtx2)+np.square(Ytx1)-np.square(Ytx2)
	self.B_1_0 = np.square(Xtx1)-np.square(Xtx3)+np.square(Ytx1)-np.square(Ytx3)
	self.B_2_0 = np.square(Xtx1)-np.square(Xtx4)+np.square(Ytx1)-np.square(Ytx4)
	
	#Initialize matrix_B and matrix_A with all zeros.
#	self.matrix_B = [[0 for col in range (1)] for row in range(3)]
	self.matrix_A = np.array([[Xtx1-Xtx2, Ytx1-Ytx2], [Xtx1-Xtx3, Ytx1-Ytx3], [Xtx1-Xtx4, Ytx1-Ytx4]])
#	self.matrix_A = [[0 for col in range (2)] for row in range(3)]
#	self.matrix_A[0][0] = Xtx1-Xtx2
#	self.matrix_A[0][1] = Ytx1-Ytx2
#	self.matrix_A[1][0] = Xtx1-Xtx3
#	self.matrix_A[1][1] = Ytx1-Ytx3
#	self.matrix_A[2][0] = Xtx1-Xtx4
#	self.matrix_A[2][1] = Ytx1-Ytx4
        gr.sync_block.__init__(self,
            name="Algorithm2",
            in_sig=[np.float32, np.float32, np.float32, np.float32],
            out_sig=[np.float32, np.float32])


    def work(self, input_items, output_items):
	#Buffer references
        in0 = input_items[0]
	in1 = input_items[1]
	in2 = input_items[2]
	in3 = input_items[3]
        out0 = output_items[0]
	out1 = output_items[1]

	#Signal processing here, process data
	#Set value of matrix_B
	self.matrix_B = (1./2.)*(np.array([[in1 - in0 + self.B_0_0], [in2 - in0 + self.B_1_0], [in3 - in0 + self.B_2_0]]))
#	self.matrix_B[0][0] = (in1 - in0 + self.B_0_0)/2
#	self.matrix_B[1][0] = (in2 - in0 + self.B_1_0)/2
#	self.matrix_B[2][0] = (in3 - in0 + self.B_2_0)/2

	
        out0[:], out1[:] = linalg.lstsq (self.matrix_A, self.matrix_B)[0]
#	out1[:] = linalg.lstsq (self.matrix_A, matrix_B)[1]
        return len(output_items[0])

