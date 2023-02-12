from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
Window.size = (310, 570)

kv = '''
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDFloatLayout:
    md_bg_color: 0, 1, 0, 9
    ScreenManager:
        id: scr
        transition: NoTransition() 
        MDScreen:
            name: "home"
            MDLabel:
                text: "Home"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "library"
            MDLabel:
                text: "Library"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "chat"
            MDLabel:
                text: "Chat"
                pos_hint: {"center_y": .5}
                halign: "center"  
        MDScreen:
            name: "home2"
            MDLabel:
                text: "Account-settings"
                pos_hint: {"center_y": .5}
                halign: "center"    
    NavBar:   
        size_hint: .85, 0.09
        pos_hint: {"center_x": .5, "center_y": .1}
        elevation: 10
        md_bg_color: 0, 1, 0, 1
        radius: [20]      
        MDGridLayout:
            cols: 4
            size_hint_x: .8
            spacing: 9
            pos_hint: {"center_x": .5, "center_y": .4}   
            MDIconButton:
                id: nav_icon1            
                icon: "home"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom" 
                text_color: 0, 0, 1, 1    
                on_release:
                    scr.current = "home" 
                    app.change_color(self) 
            MDIconButton:
                id: nav_icon2            
                icon: "library"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 1, 0, 1, 1   
                on_release:
                    scr.current = "library"
                    app.change_color(self) 
            MDIconButton:
                id: nav_icon3            
                icon: "message"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom" 
                text_color: 1, 0, 1, 1
                on_release:
                    scr.current = "chat"
                    app.change_color(self) 
            MDIconButton:
                id: nav_icon4            
                icon: "account-settings"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom" 
                text_color: 1, 0, 1, 1    
                on_release:
                    scr.current = "home2" 
                    app.change_color(self)       
'''


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class BottomNavbar(MDApp):

    def build(self):
        return Builder.load_string(kv)

    def change_color(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(4):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 0, 0, 1, 1
                else:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = 1, 0, 1, 1

if __name__ == "__main__":
    BottomNavbar().run()
