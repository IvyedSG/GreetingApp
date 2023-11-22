from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DecirHola(App):
    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}

        self.window.add_widget(Image(source="logo.png"))

        self.Saludo=Label(
            text="¿Cuál es tu nombre?",
            font_size=20,
            color='#00FFCE'
        )

        self.window.add_widget(self.Saludo)

        self.user=TextInput(
            multiline=False,
            padding_y=(20,20),
            size_hint=(1,0.5),

        )

        self.window.add_widget(self.user)

        self.button=Button(
            text="Saludar",
            size_hint=(1,0.5),
            bold=True,
            background_color="#00FFCE"
        )

        self.button.bind(on_press=self.llamado)
        self.window.add_widget(self.button)

        return self.window

    def llamado(self,instance):
        self.Saludo.text = "Hola "+ self.user.text + "!"

if __name__ == "__main__":
    DecirHola().run()
