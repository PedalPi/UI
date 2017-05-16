from kivy.lang import Builder

from ui.api.screen_page import ScreenPage


class SplashScreen(ScreenPage):
    screen = Builder.load_file('pages/splash/splash.kv')
