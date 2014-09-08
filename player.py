import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
from PyQt4.QtCore import QObject, QTimer, pyqtSignal

GObject.threads_init()
Gst.init(None)

class Player(QObject):
    currentPositionSignal = pyqtSignal(float, float)
    currentSongArtistTitleSignal = pyqtSignal(str)
    currentStateSignal = pyqtSignal(bool)

    def __init__(self, parent):
        super(Player, self).__init__(parent)
        self.playing = False
        self.player = Gst.ElementFactory.make('playbin', 'player')
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)
        self.player.connect("about-to-finish", self.on_finished)
        self.playlist = []
        self.index = 0

        self.positionTimer = QTimer(self)
        self.positionTimer.timeout.connect(self.__emitCurrentPosition__)

    def __emitCurrentPosition__(self):
        current = self.player.query_position(Gst.Format.TIME)[1] / Gst.SECOND
        duration = self.player.query_duration(Gst.Format.TIME)[1] / Gst.SECOND
        self.currentPositionSignal.emit(current, duration)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.stop()

        elif t == Gst.MessageType.ERROR:
            self.player.set_state(Gst.State.NULL)
            self.playing = False
            err, debug = message.parse_error()
            print ("Error: %s" % err, debug)

        elif t == Gst.MessageType.TAG:
            taglist = message.parse_tag()
            artist = taglist.get_string('artist')[1]
            title = taglist.get_string('title')[1]
            self.currentSongArtistTitleSignal.emit("%s (%s)" % (title, artist))

    def on_finished(self, player):
        if len (self.playlist) > self.index +1:
          self.index += 1
          self.player.set_property("uri", self.playlist[self.index])
        else:
            self.playing = False
            duration = self.player.query_duration(Gst.Format.TIME)[1] / Gst.SECOND
            self.currentPositionSignal.emit(0.0, duration)
            self.positionTimer.stop()
            self.currentStateSignal.emit(self.playing)


    def setFileList(self, playlist):
       self.playlist = playlist
       # initialize with first song from list
       self.player.set_property("uri", self.playlist[self.index])
       self.togglePlayPause()
        

    def __play__(self):
        self.player.set_state(Gst.State.PLAYING)
        self.playing = True
        self.positionTimer.start(1000)
        
    def __pause__(self):
       if not self.playing: 
          raise Exception('StateError', 'A non-playing player cannot pause')
       self.player.set_state(Gst.State.PAUSED)
       self.playing = False
       self.positionTimer.stop()
       self.__emitCurrentPosition__()

    def lastTitle(self):
       if self.index > 0:
          self.stop()
          self.index -= 1
          self.player.set_property("uri", self.playlist[self.index])
          self.togglePlayPause()
      
    def nextTitle(self):
       if len(self.playlist) > self.index +1:
          self.stop()
          self.index += 1
          self.player.set_property("uri", self.playlist[self.index])
          self.togglePlayPause()

    def togglePlayPause(self):
        if self.playing:
            self.__pause__()
        else:
            self.__play__()
        self.currentStateSignal.emit(self.playing)

    def seek(self, seek_pos):
        nanosecs = Gst.SECOND * seek_pos
        self.player.seek_simple(
                Gst.Format.TIME, 
                Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT, 
                nanosecs)

    def stop(self):
        self.playing = False
        duration = self.player.query_duration(Gst.Format.TIME)[1] / Gst.SECOND
        self.player.set_state(Gst.State.NULL)
        self.currentPositionSignal.emit(0.0, duration)
        self.positionTimer.stop()
        self.currentStateSignal.emit(self.playing)

    def incVolume(self):
       currentVol = self.player.get_property('volume')
       self.player.set_property('volume', min(1.0, currentVol + 0.1))

    def decVolume(self):
       currentVol = self.player.get_property('volume')
       self.player.set_property('volume', max(0.0, currentVol - 0.1))
