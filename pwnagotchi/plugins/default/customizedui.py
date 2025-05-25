import logging

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.components import Text
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.ui.hw as hw


WHITE = 0x00 # white is actually black on jays image
BLACK = 0xFF # black is actually white on jays image

BACKGROUND_1 = 0
FOREGROUND_1 = 1

BACKGROUND_L = 0
FOREGROUND_L = 255

BACKGROUND_BGR_16 = (0,0,0)
FOREGROUND_BGR_16 = (31,63,31)

BACKGROUND_RGB = (0,0,0)
FOREGROUND_RGB = (255,255,255)

class CustomizedUI(plugins.Plugin):
    __author__ = 'evilsocket@gmail.com'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'An customized UI plugin.'

    def __init__(self):
        self.options = dict()

    # called when http://<host>:<port>/plugins/<plugin>/ is called
    # must return a html page
    # IMPORTANT: If you use "POST"s, add a csrf-token (via csrf_token() and render_template_string)
    def on_webhook(self, path, request):
        pass

    # called when the plugin is loaded
    def on_loaded(self):
        self.mode = '1' # 1 = (1-bit pixels, black and white, stored with one pixel per byte)
        try:
            display_type = self.options["ui"]["display"]["type"]
        except Exception as e:
            logging.error("[customizedui] Missing config: main.plugins.customizedui.display.type")
        self.hw_display_config = hw.display_for(self.options)
        if hasattr(self.hw_display_config, 'mode'):
            self.mode = self.hw_display_config.mode
        
        if self.mode == '1':
            self.BACKGROUND = BACKGROUND_1
            self.FOREGROUND = FOREGROUND_1
            # do stuff is color mode is 1 when View object is created. 
        elif self.mode == 'L':
            self.BACKGROUND =  BACKGROUND_L # black 0 to 255
            self.FOREGROUND = FOREGROUND_L
            # do stuff is color mode is L when View object is created.
        elif self.mode == 'P':
            pass
            # do stuff is color mode is P when View object is created.
        elif self.mode == 'BGR;16':
            self.BACKGROUND = BACKGROUND_BGR_16 #black tuple
            self.FOREGROUND = FOREGROUND_BGR_16 #white tuple
        elif self.mode == 'RGB':
            self.BACKGROUND = BACKGROUND_RGB #black tuple
            self.FOREGROUND = FOREGROUND_RGB #white tuple
            # do stuff is color mode is RGB when View object is created.
        elif self.mode == 'RGBA':
            # do stuff is color mode is RGBA when View object is created.
            pass
        elif self.mode == 'CMYK':
            # do stuff is color mode is CMYK when View object is created.
            pass
        elif self.mode == 'YCbCr':
            # do stuff is color mode is YCbCr when View object is created.
            pass
        else:
            # do stuff when color mode doesnt exist for display
            self.BACKGROUND = BACKGROUND_1
            self.FOREGROUND = FOREGROUND_1

    # called before the plugin is unloaded
    def on_unload(self, ui):
        pass

    # called when there's internet connectivity
    def on_internet_available(self, agent):
        pass

    # called to setup the ui elements
    def on_ui_setup(self, ui):
        ui.remove_element('channel')
        ui.remove_element('aps')
        ui.remove_element('line1')
        ui.remove_element('line2')
        ui.remove_element('friend_name')
        ui.remove_element('name')
        ui.remove_element('status')
        ui.remove_element('mode')
        ui.remove_element('shakes')
        ui.add_element('shakes',  LabeledValue(label='TRAINERS ', value='0 (00)', color=self.FOREGROUND, position=self.hw_display_config._layout['channel'], label_font=fonts.Bold, text_font=fonts.Medium))

    # called when the ui is updated
    def on_ui_update(self, ui):
        pass

    # called when the hardware display setup is done, display is an hardware specific object
    def on_display_setup(self, display):
        pass

    # called when everything is ready and the main loop is about to start
    def on_ready(self, agent):
        pass

    # called when the AI finished loading
    def on_ai_ready(self, agent):
        pass

    # called when the AI finds a new set of parameters
    def on_ai_policy(self, agent, policy):
        pass

    # called when the AI starts training for a given number of epochs
    def on_ai_training_start(self, agent, epochs):
        pass

    # called after the AI completed a training epoch
    def on_ai_training_step(self, agent, _locals, _globals):
        pass

    # called when the AI has done training
    def on_ai_training_end(self, agent):
        pass

    # called when the AI got the best reward so far
    def on_ai_best_reward(self, agent, reward):
        pass

    # called when the AI got the worst reward so far
    def on_ai_worst_reward(self, agent, reward):
        pass

    # called when a non overlapping wifi channel is found to be free
    def on_free_channel(self, agent, channel):
        pass

    # called when the status is set to bored
    def on_bored(self, agent):
        pass

    # called when the status is set to sad
    def on_sad(self, agent):
        pass

    # called when the status is set to excited
    def on_excited(self, agent):
        pass

    # called when the status is set to lonely
    def on_lonely(self, agent):
        pass

    # called when the agent is rebooting the board
    def on_rebooting(self, agent):
        pass

    # called when the agent is waiting for t seconds
    def on_wait(self, agent, t):
        pass

    # called when the agent is sleeping for t seconds
    def on_sleep(self, agent, t):
        pass

    # called when the agent refreshed its access points list
    def on_wifi_update(self, agent, access_points):
        pass

    # called when the agent refreshed an unfiltered access point list
    # this list contains all access points that were detected BEFORE filtering
    def on_unfiltered_ap_list(self, agent, access_points):
        pass

    # called when the agent is sending an association frame
    def on_association(self, agent, access_point):
        pass

    # called when the agent is deauthenticating a client station from an AP
    def on_deauthentication(self, agent, access_point, client_station):
        pass

    # callend when the agent is tuning on a specific channel
    def on_channel_hop(self, agent, channel):
        pass

    # called when a new handshake is captured, access_point and client_station are json objects
    # if the agent could match the BSSIDs to the current list, otherwise they are just the strings of the BSSIDs
    def on_handshake(self, agent, filename, access_point, client_station):
        pass

    # called when an epoch is over (where an epoch is a single loop of the main algorithm)
    def on_epoch(self, agent, epoch, epoch_data):
        pass

    # called when a new peer is detected
    def on_peer_detected(self, agent, peer):
        pass

    # called when a known peer is lost
    def on_peer_lost(self, agent, peer):
        pass
