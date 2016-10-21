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

class proto_distance_ff(gr.sync_block):
    """
    docstring for block 2d_distance_ff
    """
    def __init__(self, lamb_order, rx_area, FOV, tx_ampl, CrxCtx, Htx, Trx_filter, cpc_gain, Hrx):
    
    	self.lamb_order=lamb_order
    	self.rx_area=rx_area
    	self.FOV=FOV
    	self.tx_ampl=tx_ampl
    	self.Htx=Htx
    	self.Hrx=Hrx
	if (Htx>Hrx):
    		self.height=Htx-Hrx
    	elif Htx<=Hrx:
    		self.above_max_height=1
    		self.height=self.Htx
    		#will raise an error here
    	elif Htx<=Hrx and Htx<=0:
    		self.height=-Htx
    	self.CrxCtx=CrxCtx
    	self.Trx_filter=Trx_filter
    	self.cpc_gain=cpc_gain
    	
        gr.sync_block.__init__(self,
            name="2d_distance_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
            #1 input, rx_opt_power, 2 outputs-radius from Tx and height


    def work(self, input_items, output_items):
        rx_opt_power = input_items[0]
        out = output_items[0]
 
        #From Jamesy and Consuelo
        self.factor = self.CrxCtx*(self.cpc_gain*self.rx_area*(self.tx_ampl/2.0)\
                      *self.Trx_filter*(self.lamb_order+1.0)/(2.0*numpy.pi))
                      
        out[:] = numpy.power(   (self.factor/rx_opt_power) * numpy.power( self.height,(self.lamb_order+1.0) ), (2.0/(self.lamb_order+3.00)))
        
       
        # <+signal processing here+>
      
        return len(output_items[0])

