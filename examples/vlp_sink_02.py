#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VLP MS Project
# Author: Jamesy Jean-Michel
# Description: Does Trilateration with RSS
# Generated: Wed Oct 19 11:14:47 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time
import vlp


class vlp_sink_02(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "VLP MS Project")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VLP MS Project")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "vlp_sink_02")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.z_rx = z_rx = 1.42
        self.y = y = 0
        self.x = x = 0
        self.samp_rate = samp_rate = 2000000
        self.lamb_order = lamb_order = 0.88
        self.fft_size = fft_size = 2000
        self.TXn_height = TXn_height = 2.15
        self.TXn_ampl = TXn_ampl = 0.7
        self.TX4_location = TX4_location = 1.105, 1.115, 0
        self.TX4_f = TX4_f = 400000
        self.TX3_location = TX3_location = .505, .455, 1.42
        self.TX3_f = TX3_f = 200000
        self.TX2_location = TX2_location = .505, 1.155, 0
        self.TX2_f = TX2_f = 300000
        self.TX1_location = TX1_location = 1.105, .455, 0
        self.TX1_f = TX1_f = 100000
        self.RX_area = RX_area = 1
        self.G_filter = G_filter = 1
        self.FOV_RX = FOV_RX = 90
        self.CrxCtx4 = CrxCtx4 = 1.21686524
        self.CrxCtx3 = CrxCtx3 = 1.42731873
        self.CrxCtx2 = CrxCtx2 = 1.37229190
        self.CrxCtx1 = CrxCtx1 = 1.37567074

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "2D Position")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "(x, y, z) values")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Time+freq")
        self.top_layout.addWidget(self.tab)
        self._y_range = Range(0, 2, 0.01, 0, 200)
        self._y_win = RangeWidget(self._y_range, self.set_y, "y", "counter_slider", float)
        self.top_layout.addWidget(self._y_win)
        self._x_range = Range(0, 2, 0.01, 0, 200)
        self._x_win = RangeWidget(self._x_range, self.set_x, "x", "counter_slider", float)
        self.top_layout.addWidget(self._x_win)
        self.vlp_trilat_fixed_4in_ff_0 = vlp.trilat_fixed_4in_ff((TX1_location), (TX2_location), (TX3_location), (TX4_location))
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(0, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            3
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Trilateration Output")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_0.set_min(i, -2)
            self.qtgui_number_sink_0.set_max(i, 2)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label("Relative Gain", "dB")
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_freq_sink_x_0_win)
        self.optical_2_distance_ff_3 = vlp.poptical_2_distance_ff(lamb_order, RX_area, FOV_RX, TXn_ampl, TXn_height, CrxCtx4, 1.0)
        self.optical_2_distance_ff_2 = vlp.poptical_2_distance_ff(lamb_order, RX_area, FOV_RX, TXn_ampl, TXn_height, CrxCtx3, 1.0)
        self.optical_2_distance_ff_1 = vlp.poptical_2_distance_ff(lamb_order, RX_area, FOV_RX, TXn_ampl, TXn_height, CrxCtx2, 1.0)
        self.optical_2_distance_ff_0 = vlp.poptical_2_distance_ff(lamb_order, RX_area, FOV_RX, TXn_ampl, TXn_height, CrxCtx1, 1.0)
        self.goertzel_fc_0_2 = fft.goertzel_fc(samp_rate, fft_size, TX2_f)
        self.goertzel_fc_0_1 = fft.goertzel_fc(samp_rate, fft_size, TX3_f)
        self.goertzel_fc_0_0 = fft.goertzel_fc(samp_rate, fft_size, TX4_f)
        self.goertzel_fc_0 = fft.goertzel_fc(samp_rate, fft_size, TX1_f)
        self.blocks_null_sink_3 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0_2 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, z_rx)
        self.Position = qtgui.const_sink_c(
        	1024, #size
        	"Receiver (2D) Position", #name
        	1 #number of inputs
        )
        self.Position.set_update_time(1)
        self.Position.set_y_axis(0, 1.37)
        self.Position.set_x_axis(0, 1.45)
        self.Position.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Position.enable_autoscale(False)
        self.Position.enable_grid(True)
        self.Position.enable_axis_labels(True)
        
        if not True:
          self.Position.disable_legend()
        
        labels = ["X position", "Y position", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Position.set_line_label(i, "Data {0}".format(i))
            else:
                self.Position.set_line_label(i, labels[i])
            self.Position.set_line_width(i, widths[i])
            self.Position.set_line_color(i, colors[i])
            self.Position.set_line_style(i, styles[i])
            self.Position.set_line_marker(i, markers[i])
            self.Position.set_line_alpha(i, alphas[i])
        
        self._Position_win = sip.wrapinstance(self.Position.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._Position_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.optical_2_distance_ff_0, 1))    
        self.connect((self.analog_const_source_x_0, 0), (self.optical_2_distance_ff_1, 1))    
        self.connect((self.analog_const_source_x_0, 0), (self.optical_2_distance_ff_2, 1))    
        self.connect((self.analog_const_source_x_0, 0), (self.optical_2_distance_ff_3, 1))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.goertzel_fc_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.goertzel_fc_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.goertzel_fc_0_1, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.goertzel_fc_0_2, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.optical_2_distance_ff_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.optical_2_distance_ff_3, 0))    
        self.connect((self.blocks_complex_to_mag_0_1, 0), (self.optical_2_distance_ff_2, 0))    
        self.connect((self.blocks_complex_to_mag_0_2, 0), (self.optical_2_distance_ff_1, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.Position, 0))    
        self.connect((self.goertzel_fc_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.goertzel_fc_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.goertzel_fc_0_1, 0), (self.blocks_complex_to_mag_0_1, 0))    
        self.connect((self.goertzel_fc_0_2, 0), (self.blocks_complex_to_mag_0_2, 0))    
        self.connect((self.optical_2_distance_ff_0, 1), (self.blocks_null_sink_1, 0))    
        self.connect((self.optical_2_distance_ff_0, 0), (self.vlp_trilat_fixed_4in_ff_0, 0))    
        self.connect((self.optical_2_distance_ff_1, 1), (self.blocks_null_sink_3, 0))    
        self.connect((self.optical_2_distance_ff_1, 0), (self.vlp_trilat_fixed_4in_ff_0, 1))    
        self.connect((self.optical_2_distance_ff_2, 1), (self.blocks_null_sink_2, 0))    
        self.connect((self.optical_2_distance_ff_2, 0), (self.vlp_trilat_fixed_4in_ff_0, 2))    
        self.connect((self.optical_2_distance_ff_3, 0), (self.vlp_trilat_fixed_4in_ff_0, 3))    
        self.connect((self.optical_2_distance_ff_3, 1), (self.vlp_trilat_fixed_4in_ff_0, 4))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.vlp_trilat_fixed_4in_ff_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.vlp_trilat_fixed_4in_ff_0, 1), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.vlp_trilat_fixed_4in_ff_0, 0), (self.qtgui_number_sink_0, 2))    
        self.connect((self.vlp_trilat_fixed_4in_ff_0, 1), (self.qtgui_number_sink_0, 1))    
        self.connect((self.vlp_trilat_fixed_4in_ff_0, 2), (self.qtgui_number_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "vlp_sink_02")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_z_rx(self):
        return self.z_rx

    def set_z_rx(self, z_rx):
        self.z_rx = z_rx
        self.analog_const_source_x_0.set_offset(self.z_rx)

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.goertzel_fc_0_2.set_rate(self.samp_rate)
        self.goertzel_fc_0_1.set_rate(self.samp_rate)
        self.goertzel_fc_0_0.set_rate(self.samp_rate)
        self.goertzel_fc_0.set_rate(self.samp_rate)

    def get_lamb_order(self):
        return self.lamb_order

    def set_lamb_order(self, lamb_order):
        self.lamb_order = lamb_order

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_TXn_height(self):
        return self.TXn_height

    def set_TXn_height(self, TXn_height):
        self.TXn_height = TXn_height

    def get_TXn_ampl(self):
        return self.TXn_ampl

    def set_TXn_ampl(self, TXn_ampl):
        self.TXn_ampl = TXn_ampl

    def get_TX4_location(self):
        return self.TX4_location

    def set_TX4_location(self, TX4_location):
        self.TX4_location = TX4_location

    def get_TX4_f(self):
        return self.TX4_f

    def set_TX4_f(self, TX4_f):
        self.TX4_f = TX4_f
        self.goertzel_fc_0_0.set_freq(self.TX4_f)

    def get_TX3_location(self):
        return self.TX3_location

    def set_TX3_location(self, TX3_location):
        self.TX3_location = TX3_location

    def get_TX3_f(self):
        return self.TX3_f

    def set_TX3_f(self, TX3_f):
        self.TX3_f = TX3_f
        self.goertzel_fc_0_1.set_freq(self.TX3_f)

    def get_TX2_location(self):
        return self.TX2_location

    def set_TX2_location(self, TX2_location):
        self.TX2_location = TX2_location

    def get_TX2_f(self):
        return self.TX2_f

    def set_TX2_f(self, TX2_f):
        self.TX2_f = TX2_f
        self.goertzel_fc_0_2.set_freq(self.TX2_f)

    def get_TX1_location(self):
        return self.TX1_location

    def set_TX1_location(self, TX1_location):
        self.TX1_location = TX1_location

    def get_TX1_f(self):
        return self.TX1_f

    def set_TX1_f(self, TX1_f):
        self.TX1_f = TX1_f
        self.goertzel_fc_0.set_freq(self.TX1_f)

    def get_RX_area(self):
        return self.RX_area

    def set_RX_area(self, RX_area):
        self.RX_area = RX_area

    def get_G_filter(self):
        return self.G_filter

    def set_G_filter(self, G_filter):
        self.G_filter = G_filter

    def get_FOV_RX(self):
        return self.FOV_RX

    def set_FOV_RX(self, FOV_RX):
        self.FOV_RX = FOV_RX

    def get_CrxCtx4(self):
        return self.CrxCtx4

    def set_CrxCtx4(self, CrxCtx4):
        self.CrxCtx4 = CrxCtx4

    def get_CrxCtx3(self):
        return self.CrxCtx3

    def set_CrxCtx3(self, CrxCtx3):
        self.CrxCtx3 = CrxCtx3

    def get_CrxCtx2(self):
        return self.CrxCtx2

    def set_CrxCtx2(self, CrxCtx2):
        self.CrxCtx2 = CrxCtx2

    def get_CrxCtx1(self):
        return self.CrxCtx1

    def set_CrxCtx1(self, CrxCtx1):
        self.CrxCtx1 = CrxCtx1


def main(top_block_cls=vlp_sink_02, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
