#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 


# Consuelo, 2015
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

class Distance(gr.sync_block):
    """
    docstring for block Distance
    """
    def __init__(self, order_n, A_phy, Htx, hrx, m, FOV, Psi, ampl, CtCr0, CtCr1, CtCr2, CtCr3, G_f):
	# Semi-angle at half power (degree).
#	self.tethaHalf = tethaHalf 
	# Lambertian emission order (adimensional).
#	self.order_n = -np.log(2)/(np.log(np.cos(np.deg2rad(tethaHalf))))
	#Setting the value of the Lambertian order to the one that is closest to the real application.
	#For n = 0.88, the angle at half power is equal to 68.18 degrees.
	self.order_n = order_n
	# Physical area of a detector in a PD (meters square).
#	self.radius_rx = radius_rx
#	A_phy = np.square(radius_rx)*np.pi
	self.A_phy = A_phy
	# Distance between Tx and Rx plane (meters).
	self.Htx = Htx
	self.hrx = hrx	
	htxrx = Htx-hrx
	# Internal refractive index (adimensional).
	self.m = m 
	# Field of View, 20<=FOV<=90 (degree).
	self.FOV = FOV 
	# Effective signal-collection area and optical gain concetraror (degree).
	self.Psi = Psi
	op_gain = np.square(m)/(np.square(np.sin(np.deg2rad(FOV)))) 
	#Amplitude of Transmitted power 		
	self.ampl = ampl
	self.CtCr0 = CtCr0
	self.CtCr1 = CtCr1
	self.CtCr2 = CtCr2
	self.CtCr3 = CtCr3
	self.G_f = G_f
	self.factor = (ampl*(self.order_n+1)*np.power(htxrx, self.order_n+0.75)*self.A_phy*op_gain)/(2.*2.*np.pi)
	self.factor0 = self.factor*self.CtCr0*self.G_f
	self.factor1 = self.factor*self.CtCr1*self.G_f
	self.factor2 = self.factor*self.CtCr2*self.G_f
	self.factor3 = self.factor*self.CtCr3*self.G_f

	if Psi>FOV:
		self.factor = 0
	
        gr.sync_block.__init__(self,
            name="Distance",
            in_sig=[np.float32, np.float32, np.float32, np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
	in1 = input_items[1]
	in2 = input_items[2]
	in3 = input_items[3]
	
        out0 = output_items[0]
	out1 = output_items[1]
	out2 = output_items[2]
	out3 = output_items[3]
        # <+signal processing here+>
        out0[:] = np.square(np.power(self.factor0/in0,(1./(self.order_n+2.75))))
	out1[:] = np.square(np.power(self.factor1/in1,(1./(self.order_n+2.75))))
	out2[:] = np.square(np.power(self.factor2/in2,(1./(self.order_n+2.75))))
	out3[:] = np.square(np.power(self.factor3/in3,(1./(self.order_n+2.75))))
        return len(output_items[0])

