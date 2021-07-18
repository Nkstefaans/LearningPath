from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class HelloWorldApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(MDLabel(text = "Hello World", 
                                  halign = "center",
                                  font_style = "H1",
                                  theme_text_color = "Custom",
                                  text_color = [0,100,0,100]
                                  )
                          )
        return screen
    
if __name__ == "__main__":
    HelloWorldApp().run()