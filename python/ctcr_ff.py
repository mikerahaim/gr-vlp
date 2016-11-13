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

import numpy
from gnuradio import gr

class ctcr_ff(gr.sync_block):
    """
    This block is meant to calculate CtCr values for a given transmitter-reciever. The mathematical formula used to calculate CtCr is:
    Pr/Pt = ((m+1)/2pid^2) * A^2 * cos(theta)^m+1) * CtCr. 
    By placing the reciever directly under the transmitter in question, theta equals 90 degrees, and therefore cos(theta)^m+1=1 and drops out. 
    The remainder of the terms are known. M is the Lambertian Order (lamb_order), Ptx is the power of the signal transmitted. CtCr includes reciever area, so the final equation is:
    CtCr=(Pr/Pt)*(2pi*d^2)/(m+1)(A^2)
    
    """
    def __init__(self, Ptx, lamb_order, Htx, Hrx, RX_area=1):
    	self.Ptx=Ptx
    	self.lamb_order=lamb_order
    	self.RX_area=RX_area
    	if (Htx>=Hrx):
    		self.height=Htx-Hrx
    	elif (Hrx>Htx):
    		self.height=Hrx-Htx
    	self.dsquared = numpy.power(self.height, 2)
	self.asquared = numpy.power(self.RX_area, 2)
    	   
    	gr.sync_block.__init__(self,
            name="ctcr_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = (in0/self.Ptx)*(2*numpy.pi*self.dsquared)/((self.lamb_order+1)*(self.RX_area))
        return len(input_items[0])

