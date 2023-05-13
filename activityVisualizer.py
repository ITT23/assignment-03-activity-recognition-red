# this program visualizes activities with pyglet
import numpy as np
import pyglet
from pyglet import clock
import os
from PIL import Image
from activityRecognizer import main, continous_prediction, \
    check_for_buttonclick

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

punchingImagePath = os.path.normpath("Images/punching_image.jpg")
punchingImage = pyglet.image.load(punchingImagePath)

wavingImagePath = os.path.normpath("Images/waving_image.jpg")
wavingImage = pyglet.image.load(wavingImagePath)

standingImagePath = os.path.normpath("Images/standing_image.jpg")
standingImage = pyglet.image.load(standingImagePath)


# img = Image.open(punchingImagePath)
# new_img = img.resize((800,600))
# new_img.save('Images/standing_image_60.jpg')


class Visualizer:
    def __init__(self):
        self.punchingSprite = pyglet.sprite.Sprite(img=punchingImage)
        self.wavingSprite = pyglet.sprite.Sprite(img=wavingImage)
        self.standingSprite = pyglet.sprite.Sprite(img=standingImage)
        self.currentImage = None
        self.classifier, self.encoder = main()
        self.predictions = []
        self.startScreen = True

    def draw(self):
        if self.startScreen:
            pyglet.text.Label('Welcome to the ActivityRecognizer',
                              font_name='Times New Roman',
                              font_size=36,
                              x=WINDOW_WIDTH / 2,
                              y=WINDOW_HEIGHT / 2,
                              anchor_x='center',
                              anchor_y='center').draw()
            pyglet.text.Label(
                'You can stand, wave and punch',
                font_name='Times New Roman',
                font_size=18,
                x=WINDOW_WIDTH / 2,
                y=WINDOW_HEIGHT / 2 - 50,
                anchor_x='center',
                anchor_y='center').draw()
            pyglet.text.Label('Press button_1 to start the predicitons',
                              font_name='Times New Roman',
                              font_size=18,
                              x=WINDOW_WIDTH / 2,
                              y=WINDOW_HEIGHT / 2 - 100,
                              anchor_x='center',
                              anchor_y='center').draw()
        elif not self.startScreen and not self.currentImage:
            pyglet.text.Label('Predicting...',
                              font_name='Times New Roman',
                              font_size=36,
                              x=WINDOW_WIDTH / 2,
                              y=WINDOW_HEIGHT / 2,
                              anchor_x='center',
                              anchor_y='center').draw()
        else:
            self.currentImage.draw()

    def update(self, delta_time):
        pred = continous_prediction(classifier=self.classifier,
                                    encoder=self.encoder)
        print(self.encoder.classes_[pred])

        if not self.startScreen:
            self.predictions.append(pred[0])

            if len(self.predictions) > 10:
                if self.eval_preds():
                    predCounts = np.bincount(self.predictions)
                    mostCommon = np.argmax(predCounts)
                    if mostCommon == 0:
                        self.currentImage = self.punchingSprite
                    elif mostCommon == 1:
                        self.currentImage = self.standingSprite
                    elif mostCommon == 2:
                        self.currentImage = self.wavingSprite

                self.predictions = []

    def eval_preds(self):
        # Allow 1 Wrong Input to make the detection easier
        missed = 0
        previous = self.predictions[0]
        for number in self.predictions:
            if number != previous:
                if missed == 0:
                    missed += 1
                else:
                    return False
            previous = number
        return True

    def start_predicitons(self, delta_time):
        isButtonPressed = check_for_buttonclick()
        if isButtonPressed:
            self.startScreen = False


@window.event
def on_draw():
    window.clear()
    visualizer.draw()


if __name__ == "__main__":
    visualizer = Visualizer()
    clock.schedule_interval(visualizer.update, 0.1)
    clock.schedule_interval(visualizer.start_predicitons, 0.01)
    pyglet.app.run()
