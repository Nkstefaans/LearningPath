from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

KV = '''
MDScreen:

    MDRaisedButton:
        text: "LOGIN"
        md_bg_color: 1, 0, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5} 

    MDTextField:
        hint_text: "ENTER YOUR PPASSWORD"
        halign: 'center'
        line_color_focus: 1, 0, 1, 1
        color_mode: "custom"
        pos_hint: {"center_y": 0.7}  
'''

class PasswordApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
if __name__ == "__main__":
    PasswordApp().run()