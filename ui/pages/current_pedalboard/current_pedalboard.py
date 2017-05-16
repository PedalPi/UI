from kivy.lang import Builder

from ui.api.screen_page import ScreenPage


class CurrentPedalboardScreen(ScreenPage):
    screen = Builder.load_file('pages/current_pedalboard/current_pedalboard.kv')
