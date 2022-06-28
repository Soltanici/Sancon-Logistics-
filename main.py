import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid


if __name__ == "__main__":
    MyApp().run()
