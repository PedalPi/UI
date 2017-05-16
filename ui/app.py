from kivy.lang import Builder

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window

from ui.pages.splash.splash import SplashScreen
from ui.pages.current_pedalboard.current_pedalboard import CurrentPedalboardScreen
from ui.pages.pedalboards.pedalboards import PedalboardsScreen

from kivy.clock import Clock
Window.size = (320, 240)
Window.clearcolor = (236/255, 240/255, 241/255, 1)


class PedalPiDisplayApp(App):
    icon = 'assets/images/icon.png'
    title = 'Pedal Pi'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = None

    def build(self):
        Builder.load_file('app.kv')
        self.screen_manager = self._generate_screen_manager()

        def set_current(*args):
            import random
            tela = random.choice(self.screen_manager.screen_names)
            self.screen_manager.current = tela

        #Clock.schedule_once(set_current, 2)
        #Clock.schedule_interval(set_current, .2)
        self.screen_manager.current = 'current'
        return self.screen_manager

    def _generate_screen_manager(self):
        manager = ScreenManager(transition=NoTransition())

        for screen in self._screens():
            manager.add_widget(screen)

        return manager

    def _screens(self):
        return [
            SplashScreen(name='splash'),
            CurrentPedalboardScreen(name='current'),
            PedalboardsScreen(name='pedalboards')
        ]


if __name__ == "__main__":
    PedalPiDisplayApp().run()
