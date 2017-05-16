from kivy.lang import Builder

from ui.api.screen_page import ScreenPage


class HomeScreen(ScreenPage):
    screen = Builder.load_file('pages/home/home.kv')
