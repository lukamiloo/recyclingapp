import kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty, DictProperty
from kivy.animation import Animation


class MyLayout(PageLayout):
    recycleObj = ObjectProperty(None)

    def search(self):
        file = open("testfile.txt", "r")
        st_check = self.recycleObj.text
        data = st_check.lower()
        for x in file:
            i = 0
            if data in x:
                if "Blue" in x:
                    self.ids.imageView.source = 'recycle.png'
                elif "Green" in x:
                    self.ids.imageView.source = 'compost.png'
                else:
                    self.ids.imageView.source = 'trash.png'
            else:
                i += 1
                continue
        file.close()


class MyApp(App):

    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
