import kivy
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from demo.demo import Profiles

Builder.load_file('story.kv')

Window.size = (340, 700)


class WindowManager(ScreenManager):
    """A window manager to switch between screen"""


class MessageScreen(Screen):
    """A screen that display the stories and all message histories"""


class StoryWithImage(MDBoxLayout):
    """Horizontal Layout with user dp and username"""
    text = StringProperty()  # Storing User's name
    source = StringProperty() # Path to user storing user pictures


class MainApp(MDApp):
    def build(self):
        """
        Initialize the Application and then, will return root
        :return:
        """
        self.theme_cls.theme_style = 'Dark'  # For Dark Theme.
        self.theme_cls.primary_palette = 'Teal'  # Main Color.
        self.theme_cls.accent_palette = 'Teal'  # The second color palette with 400 hue.
        self.theme_cls_accent_hue = '400'
        self.title = 'New Redesign WhatsApp'

        # """Sorting the screen in List"""
        screens = [
            MessageScreen(name='message')
        ]

        # Adding All in Screens to window manager
        self.wm = WindowManager(transition=FadeTransition())
        for screen in screens:
            self.wm.add_widget(screen)

        # Return the Window manager.
        return self.wm


if __name__ == "__main__":
    MainApp().run()
