#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VLP MS Project
# Author: Jamesy Jean-Michel
# Description: This is to TX 4 sine waves fo different frequencies via the 4 CREE luminaires in the SLURP light cage
# Generated: Mon Jul 11 11:28:51 2016
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
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
import time


class Sine_4TX(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Sine_4TX")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.TX3_FREQ = TX3_FREQ = 400e3
        self.TX3_AMPL = TX3_AMPL = 0.7
        self.TX2_FREQ = TX2_FREQ = 200e3
        self.TX2_AMPL = TX2_AMPL = 0.7
        self.TX1_FREQ = TX1_FREQ = 300e3
        self.TX1_AMPL = TX1_AMPL = 0.7
        self.TX0_FREQ = TX0_FREQ = 100e3
        self.TX0_AMPL = TX0_AMPL = 0.7

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_tab_widget_0 = Qt.QTabWidget()
        self.qtgui_tab_widget_0_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_0)
        self.qtgui_tab_widget_0_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_0.addLayout(self.qtgui_tab_widget_0_grid_layout_0)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_0, "TX0")
        self.qtgui_tab_widget_0_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_1)
        self.qtgui_tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_1.addLayout(self.qtgui_tab_widget_0_grid_layout_1)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_1, "TX1")
        self.qtgui_tab_widget_0_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_2)
        self.qtgui_tab_widget_0_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_2.addLayout(self.qtgui_tab_widget_0_grid_layout_2)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_2, "TX2")
        self.qtgui_tab_widget_0_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_3)
        self.qtgui_tab_widget_0_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_3.addLayout(self.qtgui_tab_widget_0_grid_layout_3)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_3, "TX3")
        self.top_layout.addWidget(self.qtgui_tab_widget_0)
        self._TX3_FREQ_range = Range(10e3, 10e6, 10e3, 400e3, 200)
        self._TX3_FREQ_win = RangeWidget(self._TX3_FREQ_range, self.set_TX3_FREQ, "TX3 Frequency", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_3.addWidget(self._TX3_FREQ_win)
        self._TX3_AMPL_range = Range(0, 1.0, 0.01, 0.7, 100)
        self._TX3_AMPL_win = RangeWidget(self._TX3_AMPL_range, self.set_TX3_AMPL, "TX3 Amplitude", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_3.addWidget(self._TX3_AMPL_win)
        self._TX2_FREQ_range = Range(10e3, 10e6, 10e3, 200e3, 200)
        self._TX2_FREQ_win = RangeWidget(self._TX2_FREQ_range, self.set_TX2_FREQ, "TX2 Frequency", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_2.addWidget(self._TX2_FREQ_win)
        self._TX2_AMPL_range = Range(0, 1.0, 0.01, 0.7, 100)
        self._TX2_AMPL_win = RangeWidget(self._TX2_AMPL_range, self.set_TX2_AMPL, "TX2 Amplitude", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_2.addWidget(self._TX2_AMPL_win)
        self._TX1_FREQ_range = Range(10e3, 10e6, 10e3, 300e3, 200)
        self._TX1_FREQ_win = RangeWidget(self._TX1_FREQ_range, self.set_TX1_FREQ, "TX1 Frequency", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_1.addWidget(self._TX1_FREQ_win)
        self._TX1_AMPL_range = Range(0, 1.0, 0.01, 0.7, 100)
        self._TX1_AMPL_win = RangeWidget(self._TX1_AMPL_range, self.set_TX1_AMPL, "TX1 Amplitude", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_1.addWidget(self._TX1_AMPL_win)
        self._TX0_FREQ_range = Range(10e3, 10e6, 10e3, 100e3, 200)
        self._TX0_FREQ_win = RangeWidget(self._TX0_FREQ_range, self.set_TX0_FREQ, "TX0 Frequency", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_0.addWidget(self._TX0_FREQ_win)
        self._TX0_AMPL_range = Range(0, 1.0, 0.01, 0.7, 100)
        self._TX0_AMPL_win = RangeWidget(self._TX0_AMPL_range, self.set_TX0_AMPL, "TX0 Amplitude", "counter_slider", float)
        self.qtgui_tab_widget_0_layout_0.addWidget(self._TX0_AMPL_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_center_freq(0, 1)
        self.uhd_usrp_sink_0.set_gain(0, 1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX3_FREQ, TX3_AMPL, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX2_FREQ, TX2_AMPL, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, TX1_FREQ, TX1_AMPL, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, TX0_FREQ, TX0_AMPL, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.uhd_usrp_sink_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Sine_4TX")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_TX3_FREQ(self):
        return self.TX3_FREQ

    def set_TX3_FREQ(self, TX3_FREQ):
        self.TX3_FREQ = TX3_FREQ
        self.analog_sig_source_x_3.set_frequency(self.TX3_FREQ)

    def get_TX3_AMPL(self):
        return self.TX3_AMPL

    def set_TX3_AMPL(self, TX3_AMPL):
        self.TX3_AMPL = TX3_AMPL
        self.analog_sig_source_x_3.set_amplitude(self.TX3_AMPL)

    def get_TX2_FREQ(self):
        return self.TX2_FREQ

    def set_TX2_FREQ(self, TX2_FREQ):
        self.TX2_FREQ = TX2_FREQ
        self.analog_sig_source_x_2.set_frequency(self.TX2_FREQ)

    def get_TX2_AMPL(self):
        return self.TX2_AMPL

    def set_TX2_AMPL(self, TX2_AMPL):
        self.TX2_AMPL = TX2_AMPL
        self.analog_sig_source_x_2.set_amplitude(self.TX2_AMPL)

    def get_TX1_FREQ(self):
        return self.TX1_FREQ

    def set_TX1_FREQ(self, TX1_FREQ):
        self.TX1_FREQ = TX1_FREQ
        self.analog_sig_source_x_1.set_frequency(self.TX1_FREQ)

    def get_TX1_AMPL(self):
        return self.TX1_AMPL

    def set_TX1_AMPL(self, TX1_AMPL):
        self.TX1_AMPL = TX1_AMPL
        self.analog_sig_source_x_1.set_amplitude(self.TX1_AMPL)

    def get_TX0_FREQ(self):
        return self.TX0_FREQ

    def set_TX0_FREQ(self, TX0_FREQ):
        self.TX0_FREQ = TX0_FREQ
        self.analog_sig_source_x_0.set_frequency(self.TX0_FREQ)

    def get_TX0_AMPL(self):
        return self.TX0_AMPL

    def set_TX0_AMPL(self, TX0_AMPL):
        self.TX0_AMPL = TX0_AMPL
        self.analog_sig_source_x_0.set_amplitude(self.TX0_AMPL)


def main(top_block_cls=Sine_4TX, options=None):

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
