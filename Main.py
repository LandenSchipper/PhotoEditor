from kivy.app import App
from kivy.uix.screenmanager import Screen

class PhotoEditorApp(App):
    def build(self):
        return Display()

class Display(Screen):
    def display_image(self):

        self.ids.IMG.source = self.ids.ans.text


PhotoEditorApp().run()
