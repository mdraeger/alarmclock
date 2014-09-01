import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
from PyQt4.QtCore import QObject, pyqtSignal

GObject.threads_init()
Gst.init(None)

class Player(QObject):
    currentPositionSignal = pyqtSignal(float, float)
    currentSongTitleSignal = pyqtSignal(ststr)
    currentStateSignal = pyqtSignal(bool)

    def __init__(self, uri):
        self.playing = False
        self.player = Gst.ElementFactory.make('playbin', 'player')
        bus = self.player.get_bus()
        bus.connect("message", self.on_message)
        self.player.connect("about-to-finish", self.on_finished)
        self.currentUri = uri
        self.__emitCurrentPosition__()

    def __emitCurrentPosition__(self):
        current = self.player.query_position(Gst.Format.TIME)[1] / Gst.SECOND
        duration = self.player.query_duration(Gst.Format.TIME)[1] / Gst.SECOND
        self.currentPositionSignal.emit(current, duration)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.Message.EOS:
            self.player.set_state(Gst.State.NULL)
            self.playing = False

        elif t == Gst.Message.ERROR:
            self.player.set_state(Gst.State.NULL)
            self.playing = False
            err, debug = message.parse_error()
            print ("Error: %s" % err, debug)

    def __play__(self):
        self.player.set_property("uri", self.currentUri)
        self.player.set_state(Gst.State.PLAYING)
        self.playing = True
        GObject.timeout_add(1000, self.__emitCurrentPosition__)
        
    def __pause__(self):
        if not self.playing: 
            raise Exception('StateError', 'A non-playing player cannot pause')
        self.player.set_state(Gst.State.PAUSED)
        self.playing = False
        self.__emitCurrentPosition__()

    def togglePlayPause(self):
        if self.playing:
            self.__pause__()
        else:
            self.__play__()

    def stop(self):
        self.playing = False
        duration = self.player.query_duration(Gst.Format.TIME)[1] / Gst.SECOND
        self.player.set_state(Gst.State.NULL)
        self.currentPositionSignal.emit(0.0, duration)
