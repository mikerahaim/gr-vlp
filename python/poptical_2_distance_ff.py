#!/usr/bin/env python
# Line above tells the shell that this file is a Python file and
# to use the Python interpreter to run this file. 
# Should always be included at the top to run from the terminal. 

# The comments below were mostly auto-generated by gr_modtool
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Jamesy Jean-Michel, Lighting Enabled Systems and Applications
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

# The following two lines of code tells Python the modules to include.
# We must always have gr to run GNU Radio applications. NumPy is the
# fundamental package for scientific computing with Python. It contains
# among other things: a powerful N-dimentsional array object, useful
# linear algebra, fourier transform, and random number capabilities.
# PEP8 tells us we should import every module on its own line. 
import numpy
from gnuradio import gr

# Define a class called "poptical_2_distance_ff" which is derived from another class, gr.sync_block. 
class poptical_2_distance_ff(gr.sync_block):
    """ The Poptical_2_Distance_ff block
    This is a sync block with 2 inputs and 1 output.
    It essetially converts an optical Power {in0} input into a Distance^2
    (radius^2) from the center of an optical transmitter modelled as a
    point source at some fixed location. This block assumes a fixed
    orientation (or elevation angle) for the receiver such that the
    angle of emission from the tranmitter (theta) equals the angle of
    incidence of the receiver (psi).
    The second input is a feedback input that adjust to the real height
    of the receiver relative of the plane of transmitters. In case of a
    fixed receiver height, set this second input to the fixed height.
    
    Lambertian Order:
    This is a unitless number between 0-1 indicating how much the
    transmitter (modelled as a point source) obey's lambert's law.
    A source which obeys Lambert's law has the same radiance when
    viewed from any angle. For a perfect lambertian source/surface,
    Lambertian Order = 1.
    
    Receiver Area:
    This is the area of the receiver's light collecting surface in
    units of meters squared (m^2).
    
    Receiver Field-of-View (FOV)
    The FOV is the (2D) angle from a line perpendicular to the surface
    of the receiver. This is also used to calculate the gain from a
    compound parabolic concentrator while assuming a refractive index
    n = 1.00 for a receiver in air.
    
    Transmitted Amplitude:
    In this system, the tranmitters are LED luminaires used as beacons
    transmitting sinusoids of unique frequencies. This field expects
    the peak-to-peak amplitude of the transmitted sinusoids.
    
    Transmitters' Height:
    In this system, all the tranmitters are assumed to lie on the same
    plane, Z=0. This field expects the height from the floor of a room
    to the plane of transmitters above the floor.
    
    Electrical Conversion Constant:
    This constant is a conversion factor that allows converting between
    electrical and optical domain and vice versa. It incorporates both
    tx->optical and optical->rx factors into one constant.
    
    Filter Spectral Transmittance
    The spectral transmittance is the ratio of the tranmitted [exiting]
    spectral flux to the incident [incoming] spectral flux of the
    illumination seen through the filter. Assume 1 for no filter.
    """
    # The (private) member function "__init__()" is called immediatly to
    # initialize the poptical_2_distance_ff class - which already exist.
    # The first argument of every class method, including __init__, is always
    # a reference to the current instance of the class. By convention, this
    # argument is always named self. In the __init__ method, self refers to
    # the newly created object; in other class methods, it refers to the
    # instance whose method was created.
    # (In OOP, a method is a function associated with an object)
    def __init__(self, lamb_order, rx_area, rx_fov, tx_ampl, tx_height, CrxCtx, Trx_filter):
        # This is the lambertian order of the tranmitter(s)
        # The transmitters are assumed to be a point source with the same
        # radiation pattern from all directions in a hemisphere radiating down
        self.lamb_order = lamb_order
        # The (light collecting) area of the receiver in the system in m^2
        self.rx_area = rx_area
        # The Field of View of the receiver in the system - likely <= 90 deg
        self.rx_fov = rx_fov
        # The amplitude of the transmitted sinusoid from the beacon
        self.tx_ampl = tx_ampl
        # The height between the plane of transmitters and the room floor
        self.tx_height = tx_height
        # Constant for converting optical power to electrical power
        self.CrxCtx = CrxCtx
        # The spectral tranmittance, is the ratio of the transmitted spectral
        # flux to the incident spectral flux seen through the RX filter
        # It is essentially an optical "gain" unlikely to be >1
        self.Trx_filter = Trx_filter
        # The parent constructor is called (in Python, this needs to be done
        # explicitly. Most things in Python need to be done explicitly ...)
        gr.sync_block.__init__(self,
            name="poptical_2_distance_ff",
            # 2 scalar inputs; 1 for p_optical. 1 for height_fb
            in_sig=[numpy.float32, numpy.float32],
            # 2 scalar outputs; 1 for distance (or radius from TX point), 1 for z element of RX
            out_sig=[numpy.float32, numpy.float32])


    def work(self, input_items, output_items):
        # This is the DC filtered (Fc = 700Hz) input to the receive USRP
        in0 = input_items[0]
        # This is the height feedback input to the GRC block
        # In case the receiver will be at a fixed height, input a constant
        in1 = input_items[1]
        # This is the distance output of the block in meters
        out0 = output_items[0]
        # This is the distance output of the block in meters
        z = output_items[1]
        # <+signal processing here+>
        # According to erro i got about code below:
        ## ValueError: The truth value of an array with more than one element is ambiguous.
        ## Use a.any() or a.all()
##        if in1 == 0:    # if height input = 0
##            in1 = 1	# make it one. Useful for initialization flow purposes

	# Initialize maximum height violation error check variable to false
        self.above_max_height = 0
        # Error checking on the height (Not doing anything yet if it's wrong)
        if height_fb > self.tx_height:
            self.above_max_height = 1   # will eventually be used to warn the user etc.
	height_fb = self.tx_height # overriding the height feedback to real max

        # There is no concentrator (cpc) lens in the design - so assume gain=1
        cpc_gain = 1.0
        # The following is the constant part of distance algorithm - see log
        self.factor = self.CrxCtx*(cpc_gain*self.rx_area*(self.tx_ampl/2.0)\
                      *self.Trx_filter*(self.lamb_order+1.0)/(2.0*numpy.pi))
        # Distance^2 = ..., because next steps needs d^2. )
        # The 0.75 (instead of 1) is a calibration factor from Consuelo's work
        out0[:] = numpy.power(((self.factor/in0)*numpy.power((self.tx_height - in1),\
                                                            (self.lamb_order+1.0))\
                              ), (2.0/(self.lamb_order+3.00)))                          # 2.75 here. 0.75 above
        # Pass through the distance input, should update after 1 block delay
        z[:] = height_fb
        return len(output_items[0])
