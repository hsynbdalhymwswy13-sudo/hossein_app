from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import os

class GalleryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main = BoxLayout(orientation="vertical")

        title = Button(
            text="🖼️  گالری حسین",
            size_hint_y=None,
            height=65,
            font_size=24
        )
        self.main.add_widget(title)

        buttons = BoxLayout(
            size_hint_y=None,
            height=55
        )

        photos = Button(text="📷 تصاویر")
        albums = Button(text="📁 آلبوم‌ها")
        favorites = Button(text="❤️ علاقه‌مندی‌ها")

        photos.bind(on_press=self.show_photos)

        buttons.add_widget(photos)
        buttons.add_widget(albums)
        buttons.add_widget(favorites)

        self.main.add_widget(buttons)

        self.scroll = ScrollView()
        self.grid = GridLayout(
            cols=3,
            spacing=5,
            padding=5,
            size_hint_y=None
        )
        self.grid.bind(minimum_height=self.grid.setter("height"))

        self.scroll.add_widget(self.grid)
        self.main.add_widget(self.scroll)

        self.add_widget(self.main)

    def show_photos(self, instance):
        self.grid.clear_widgets()

        folders = [
            os.path.expanduser("~/storage/shared/DCIM"),
            os.path.expanduser("~/storage/shared/Pictures")
        ]

        extensions = (".jpg", ".jpeg", ".png", ".webp")

        for folder in folders:
            if not os.path.exists(folder):
                continue

            for root, dirs, files in os.walk(folder):
                for filename in files:
                    if filename.lower().endswith(extensions):
                        path = os.path.join(root, filename)

                        image = Image(
                            source=path,
                            size_hint_y=None,
                            height=120,
                            allow_stretch=True,
                            keep_ratio=True
                        )

                        self.grid.add_widget(image)


class HosseinApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)

        manager = ScreenManager()
        manager.add_widget(GalleryScreen(name="gallery"))

        return manager


HosseinApp().run()
