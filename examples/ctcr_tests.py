#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: CtCr Tests
# Author: Rich McAllister
# Generated: Sat Nov 12 14:36:28 2016
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import vlp


class ctcr_tests(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "CtCr Tests")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("CtCr Tests")
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

        self.settings = Qt.QSettings("GNU Radio", "ctcr_tests")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.lamb_order = lamb_order = 0.88
        self.fft_size = fft_size = 2000
        self.TX_height = TX_height = 1.375
        self.TX_ampl = TX_ampl = 0.7
        self.TX4_f = TX4_f = 400000
        self.TX3_f = TX3_f = 200000
        self.TX2_f = TX2_f = 300000
        self.TX1_f = TX1_f = 100000
        self.RX_height = RX_height = 0
        self.RX_area = RX_area = 0.78539816339

        ##################################################
        # Blocks
        ##################################################
        self.vlp_ctcr_ff_3 = vlp.ctcr_ff(lamb_order, TX_ampl, TX_height, RX_height, RX_area)
        self.vlp_ctcr_ff_2 = vlp.ctcr_ff(lamb_order, TX_ampl, TX_height, RX_height, RX_area)
        self.vlp_ctcr_ff_1 = vlp.ctcr_ff(lamb_order, TX_ampl, TX_height, RX_height, RX_area)
        self.vlp_ctcr_ff_0 = vlp.ctcr_ff(lamb_order, TX_ampl, TX_height, RX_height, RX_area)
        self.qtgui_number_sink_3 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_3.set_update_time(0.10)
        self.qtgui_number_sink_3.set_title("CtCr4")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_3.set_min(i, -1)
            self.qtgui_number_sink_3.set_max(i, 1)
            self.qtgui_number_sink_3.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_3.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_3.set_label(i, labels[i])
            self.qtgui_number_sink_3.set_unit(i, units[i])
            self.qtgui_number_sink_3.set_factor(i, factor[i])
        
        self.qtgui_number_sink_3.enable_autoscale(False)
        self._qtgui_number_sink_3_win = sip.wrapinstance(self.qtgui_number_sink_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_3_win)
        self.qtgui_number_sink_2 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_2.set_update_time(0.10)
        self.qtgui_number_sink_2.set_title("CtCr3")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_2.set_min(i, -1)
            self.qtgui_number_sink_2.set_max(i, 1)
            self.qtgui_number_sink_2.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_2.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_2.set_label(i, labels[i])
            self.qtgui_number_sink_2.set_unit(i, units[i])
            self.qtgui_number_sink_2.set_factor(i, factor[i])
        
        self.qtgui_number_sink_2.enable_autoscale(False)
        self._qtgui_number_sink_2_win = sip.wrapinstance(self.qtgui_number_sink_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_2_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("CtCr2")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("CtCr1")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.goertzel_fc_0_2 = fft.goertzel_fc(int(samp_rate), fft_size, TX1_f)
        self.goertzel_fc_0_1 = fft.goertzel_fc(int(samp_rate), fft_size, TX2_f)
        self.goertzel_fc_0_0 = fft.goertzel_fc(int(samp_rate), fft_size, TX3_f)
        self.goertzel_fc_0 = fft.goertzel_fc(int(samp_rate), fft_size, TX4_f)
        self.blocks_throttle_3 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_source_0_2 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/rich/CTCR_testing/ctcr2_nolenses", True)
        self.blocks_file_source_0_1 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/rich/CTCR_testing/ctcr3_nolenses", True)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/rich/CTCR_testing/ctcr4_nolenses", True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/rich/CTCR_testing/ctcr1_nolenses", True)
        self.blocks_complex_to_mag_3 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_2 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_3 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_2 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 3))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.goertzel_fc_0_2, 0))    
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_null_sink_0, 2))    
        self.connect((self.blocks_complex_to_float_1, 0), (self.goertzel_fc_0_1, 0))    
        self.connect((self.blocks_complex_to_float_2, 1), (self.blocks_null_sink_0, 1))    
        self.connect((self.blocks_complex_to_float_2, 0), (self.goertzel_fc_0_0, 0))    
        self.connect((self.blocks_complex_to_float_3, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_complex_to_float_3, 0), (self.goertzel_fc_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.vlp_ctcr_ff_0, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.vlp_ctcr_ff_1, 0))    
        self.connect((self.blocks_complex_to_mag_2, 0), (self.vlp_ctcr_ff_2, 0))    
        self.connect((self.blocks_complex_to_mag_3, 0), (self.vlp_ctcr_ff_3, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_3, 0))    
        self.connect((self.blocks_file_source_0_1, 0), (self.blocks_throttle_2, 0))    
        self.connect((self.blocks_file_source_0_2, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.blocks_complex_to_float_1, 0))    
        self.connect((self.blocks_throttle_2, 0), (self.blocks_complex_to_float_2, 0))    
        self.connect((self.blocks_throttle_3, 0), (self.blocks_complex_to_float_3, 0))    
        self.connect((self.goertzel_fc_0, 0), (self.blocks_complex_to_mag_3, 0))    
        self.connect((self.goertzel_fc_0_0, 0), (self.blocks_complex_to_mag_2, 0))    
        self.connect((self.goertzel_fc_0_1, 0), (self.blocks_complex_to_mag_1, 0))    
        self.connect((self.goertzel_fc_0_2, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.vlp_ctcr_ff_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.vlp_ctcr_ff_1, 0), (self.qtgui_number_sink_1, 0))    
        self.connect((self.vlp_ctcr_ff_2, 0), (self.qtgui_number_sink_2, 0))    
        self.connect((self.vlp_ctcr_ff_3, 0), (self.qtgui_number_sink_3, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ctcr_tests")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.goertzel_fc_0_2.set_rate(int(self.samp_rate))
        self.goertzel_fc_0_1.set_rate(int(self.samp_rate))
        self.goertzel_fc_0_0.set_rate(int(self.samp_rate))
        self.goertzel_fc_0.set_rate(int(self.samp_rate))
        self.blocks_throttle_3.set_sample_rate(self.samp_rate)
        self.blocks_throttle_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_lamb_order(self):
        return self.lamb_order

    def set_lamb_order(self, lamb_order):
        self.lamb_order = lamb_order

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_TX_height(self):
        return self.TX_height

    def set_TX_height(self, TX_height):
        self.TX_height = TX_height

    def get_TX_ampl(self):
        return self.TX_ampl

    def set_TX_ampl(self, TX_ampl):
        self.TX_ampl = TX_ampl

    def get_TX4_f(self):
        return self.TX4_f

    def set_TX4_f(self, TX4_f):
        self.TX4_f = TX4_f
        self.goertzel_fc_0.set_freq(self.TX4_f)

    def get_TX3_f(self):
        return self.TX3_f

    def set_TX3_f(self, TX3_f):
        self.TX3_f = TX3_f
        self.goertzel_fc_0_0.set_freq(self.TX3_f)

    def get_TX2_f(self):
        return self.TX2_f

    def set_TX2_f(self, TX2_f):
        self.TX2_f = TX2_f
        self.goertzel_fc_0_1.set_freq(self.TX2_f)

    def get_TX1_f(self):
        return self.TX1_f

    def set_TX1_f(self, TX1_f):
        self.TX1_f = TX1_f
        self.goertzel_fc_0_2.set_freq(self.TX1_f)

    def get_RX_height(self):
        return self.RX_height

    def set_RX_height(self, RX_height):
        self.RX_height = RX_height

    def get_RX_area(self):
        return self.RX_area

    def set_RX_area(self, RX_area):
        self.RX_area = RX_area


def main(top_block_cls=ctcr_tests, options=None):

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
