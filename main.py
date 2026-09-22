from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
import os
class GalleryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(Label(text="گالری حسین", size_hint_y=None, height=60))
        self.layout.add_widget(Button(text="📷 تصاویر"))
        self.layout.add_widget(Button(text="📁 آلبوم‌ها"))
        self.layout.add_widget(Button(text="❤️ علاقه‌مندی‌ها"))
        self.layout.add_widget(Button(text="🔍 جست‌وجو"))
        self.layout.add_widget(Button(text="🗑️ سطل زباله"))
        self.add_widget(self.layout)
class HosseinApp(App):
    def build(self):
        return GalleryScreen()
HosseinApp().run()
