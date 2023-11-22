from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DecirHola(App):
    def build(self):

        return self.window
if __name__ == "__main__":
    DecirHola().run()
