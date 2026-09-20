from kivy.app import App
from kivy.uix.label import Label


class HosseinApp(App):
    def build(self):
        return Label(text="گالری حسین")


HosseinApp().run()
