from ui.api.screen_page import ScreenPage

from kivy.lang import Builder


class PedalboardsScreen(ScreenPage):
    screen = Builder.load_file('pages/pedalboards/pedalboards.kv')
