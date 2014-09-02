# Alarmclock application

## Purpose

This little application resembles a very simple alarm clock that uses the gstreamer as backend. On the pi I connected gstreamer with omx to exploit the hardware acceleration.

It is intended to run on my daughter's Raspberry Pi which is embedded in her LEGO Friends motor yacht.
The gui is optimized for a 320x240 LCD display with touch input. 

## Requirements
The player requires Gstreamer-1.0 or later and the python-gobject bindings install for Python3. Also Qt4.

## Design

The design was created with Qt designer, the analog clock widget is hand written, taken from [here!](http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/examples/designer/plugins/widgets/analogclock.py)
