from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
import math
from os import name
from PIL import Image, ImageDraw
import random
class PhotoEditorApp(App):
    def build(self):
        return Display()

class Display(Screen):
    def pointillism(self, image, num_dots=6000, dot_size_range=(3, 5)):
        width, height = image.size
        pixels = image.load()
        canvas = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(canvas)
        for _ in range(num_dots):
            size = random.randint(dot_size_range[0], dot_size_range[1])
            x = random.randint(0, width - size)
            y = random.randint(0, height - size)
            ellipse_box = [(x, y), (x + size, y + size)]
            draw.ellipse(ellipse_box, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
        del draw
        return canvas
    def apply_point(self):
        input_image = Image.open( self.ids.IMG.source)
        output_image = self.pointillism(input_image)
        output_image.save("Pointillism.png")
        self.ids.IMG.source =
    def display_image(self):

        self.ids.IMG.source = self.ids.ans.text
    cordinates = []
    def on_touch_down(self, touch):
        x, y = touch.x, touch.y
        self.cordinates.append(x)
        self.cordinates.append(y)
        if len(self.cordinates) >4 :
            self.cordinates = self.cordinates[2:]
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_down(touch)
        touch.pop()
        return ret
PhotoEditorApp().run()
