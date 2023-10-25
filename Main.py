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
image = ""
class Display(Screen):
    def red_filter(self):
        image = Image.open(self.ids.IMG.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = 255 + pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        image.save("red.png")
        self.ids.IMG.source = "red.png"

    def invert(self):
        img = Image.open(self.ids.IMG.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save("inverted.png")
        self.ids.IMG.source = "inverted.png"

    cordinates = []

    # def pixelate(self):
    #     img = Image.open(self.ids.IMG.source)
    #     height = img.height
    #     width = img.width
    #     pixels = img.load()
    #     x1,y1 = self.cordinates[0], self.cordinates[1]
    #     x2, y2 = self.cordinates[0], self.cordinates[1]
    #     for yy in range():
    #         for xx in range(x, x + width, 10):
    #             color = pixels[xx, yy]
    #             for _y in range(yy, yy + 10):
    #                 for _x in range(xx, xx + 10):
    #                     pixels[_x, _y] = color
    #     img.save("pixelate.jpg")
    def pointillism(self, num_dots=25000, dot_size_range=(40, 50)):
        image = Image.open(self.ids.IMG.source)
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
        canvas.save("Pointillism.png")
        self.ids.IMG.source = "Pointillism.png"

    def sepia(self):
        image = Image.open(self.ids.IMG.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                red = red * .393 + green * 0.769 + blue * 0.189
                green = red * .349 + green * 0.686 + blue * 0.168
                blue = red * .272 + green * 0.534 + blue * 0.131
                pixels[x, y] = (round(red), round(green), round(blue))
        image.save("sepia.png")
        self.ids.IMG.source = "sepia.png"

    def blue_to_green(self):
        image = Image.open(self.ids.IMG.source)
        pixels = image.load()
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                if pixels[x, y][2] > pixels[x, y][1]:
                    red = int(pixels[x, y][2] * 0.25)
                    green = int(pixels[x, y][2] * 1)
                    blue = int(pixels[x, y][2] * 0.75)
                    pixels[x, y] = (red, green, blue)
                else:
                    pass
        image.save("blue.png")
        self.ids.IMG.source = "blue.png"
    def display_image(self):

        self.ids.IMG.source = self.ids.ans.text

    def loadImage(self):
        return image
    def on_touch_down(self, touch):
        x, y = touch.x, touch.y
        self.cordinates.append(x)
        self.cordinates.append(y)
        if len(self.cordinates) >4 :
            self.cordinates = self.cordinates[2:]
        print("MOUSE pressed x: "+str(int(x))+" y: "+str(int(y)))
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_down(touch)
        touch.pop()
        return ret
    def on_touch_up(self, touch):
        x, y = touch.x, touch.y
        self.cordinates.append(x)
        self.cordinates.append(y)
        if len(self.cordinates) > 4:
            self.cordinates = self.cordinates[2:]
        print("MOUSE released x: " + str(int(x)) + " y: " + str(int(y)))
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_up(touch)
        touch.pop()
        return ret
PhotoEditorApp().run()
