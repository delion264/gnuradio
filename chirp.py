#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import math
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class chirp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "chirp")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 50000000
        self.rx_delay = rx_delay = 50000000
        self.fft_size = fft_size = 4096
        self.doppler_shift = doppler_shift = 0
        self.chirp_rate = chirp_rate = 2
        self.chirp_bw = chirp_bw = 2000000

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(2000000, 100000000, 1, 50000000, 200)
        self._samp_rate_win = GrRangeWidget(self._samp_rate_range, self.set_samp_rate, "'samp_rate'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._samp_rate_win)
        self._rx_delay_range = Range(10000000, 100000000, 1, 50000000, 200)
        self._rx_delay_win = GrRangeWidget(self._rx_delay_range, self.set_rx_delay, "'rx_delay'", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._rx_delay_win)
        self._doppler_shift_range = Range((-1000000), 1000000, 1, 0, 200)
        self._doppler_shift_win = GrRangeWidget(self._doppler_shift_range, self.set_doppler_shift, "'doppler_shift'", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._doppler_shift_win)
        self._chirp_rate_range = Range(1, 10000, 1, 2, 200)
        self._chirp_rate_win = GrRangeWidget(self._chirp_rate_range, self.set_chirp_rate, "'chirp_rate'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._chirp_rate_win)
        self._chirp_bw_range = Range(10000, 20000000, 5, 2000000, 200)
        self._chirp_bw_win = GrRangeWidget(self._chirp_bw_range, self.set_chirp_bw, "'chirp_bw'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._chirp_bw_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            4096, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate*2), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.05)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(True)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(True)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.fft_vxx_1 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), True, 2)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), True, 2)
        self.blocks_vector_to_stream_1_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 1, 1)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(fft_size)
        self.blocks_integrate_xx_0 = blocks.integrate_cc(500, fft_size)
        self.blocks_freqshift_cc_0 = blocks.rotator_cc(2.0*math.pi*doppler_shift/samp_rate)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, rx_delay)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, chirp_rate, chirp_bw, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_freqshift_cc_0, 0))
        self.connect((self.blocks_freqshift_cc_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_vector_to_stream_1_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_vector_to_stream_1_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "chirp")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*self.doppler_shift/self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, (self.samp_rate*2))

    def get_rx_delay(self):
        return self.rx_delay

    def set_rx_delay(self, rx_delay):
        self.rx_delay = rx_delay
        self.blocks_delay_0.set_dly(self.rx_delay)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*self.doppler_shift/self.samp_rate)

    def get_chirp_rate(self):
        return self.chirp_rate

    def set_chirp_rate(self, chirp_rate):
        self.chirp_rate = chirp_rate
        self.analog_sig_source_x_1.set_frequency(self.chirp_rate)

    def get_chirp_bw(self):
        return self.chirp_bw

    def set_chirp_bw(self, chirp_bw):
        self.chirp_bw = chirp_bw
        self.analog_sig_source_x_1.set_amplitude(self.chirp_bw)




def main(top_block_cls=chirp, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
