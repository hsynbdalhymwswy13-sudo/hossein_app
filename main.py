from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.utils import platform


class HosseinGallery(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="گالری حسین",
            font_size=28,
            size_hint_y=None,
            height=60
        )

        self.photo = Image(
            allow_stretch=True,
            keep_ratio=True
        )

        button = Button(
            text="انتخاب عکس از گوشی",
            font_size=22,
            size_hint_y=None,
            height=70
        )

        button.bind(on_press=self.choose_photo)

        layout.add_widget(title)
        layout.add_widget(self.photo)
        layout.add_widget(button)

        return layout

    def choose_photo(self, instance):
        if platform == "android":
            from android import activity
            from jnius import autoclass

            Intent = autoclass("android.content.Intent")

            intent = Intent(Intent.ACTION_OPEN_DOCUMENT)
            intent.addCategory(Intent.CATEGORY_OPENABLE)
            intent.setType("image/*")

            activity.bind(on_activity_result=self.on_result)
            activity.startActivityForResult(intent, 100)

    def on_result(self, request_code, result_code, intent):
        if request_code == 100 and intent:
            uri = intent.getData()

            if uri:
                self.photo.source = uri.toString()
                self.photo.reload()


HosseinGallery().run()
