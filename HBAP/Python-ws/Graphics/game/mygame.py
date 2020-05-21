import pygame
import random
import numpy as np
import logging


WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
RED   = (255,   0,   0)
GREEN = (  0, 225,   0)


class Blob():
    def __init__(self, color, x_bound, y_bound, size_range=(4, 8), movement_range=(-1, 2)):
        self.movement_range = movement_range
        self.X_BOUND = x_bound
        self.Y_BOUND = y_bound
        self.x = random.randrange(0, self.X_BOUND)
        self.y = random.randrange(0, self.Y_BOUND)
        self.color = color
        self.size = random.randrange(size_range[0], size_range[1])
        self.move_x = 0
        self.move_y = 0

    def move(self):
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.X_BOUND:
            self.x = self.X_BOUND

        if self.y < 0:
            self.y = 0
        elif self.y > self.Y_BOUND:
            self.y = self.Y_BOUND


class BlueBlob(Blob):
    def __init__(self, x_bound, y_bound):
        super().__init__(BLUE, x_bound, y_bound)

    # This is an unintuitive use of the __add__ method as it doesn't return anything
    def __add__(self, other_blob):
        logging.info('Blob add op {} + {}'.format(str(self.color), str(other_blob.color)))
        if other_blob.color == RED:
            self.size += other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == GREEN:
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == BLUE:
            pass
        else:
            raise Exception('Tried to combine blobs of weird colors')


class RedBlob(Blob):
    def __init__(self, x_bound, y_bound):
        super().__init__(RED, x_bound, y_bound)


class GreenBlob(Blob):
    def __init__(self, x_bound, y_bound):
        super().__init__(GREEN, x_bound, y_bound)


def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x, b2.y])) < (b1.size+b2.size)


def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                log_string = 'Checking if blobs are touching {} + {}'.format(str(blue_blob.color),
                                                                             str(other_blob.color))
                logging.debug(log_string)
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if blue_blob.size <= 0:
                            del blues[blue_id]
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
    return blues, reds, greens


def draw_environment(game_display, blob_list):
    game_display.fill(WHITE)
    blues, reds, greens = handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            # 'blob' is nu object met id
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            # for location and size of drawing
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds, greens


def main():
    starting_blue_blobs = 20
    starting_red_blobs = 10
    starting_green_blobs = 10

    width = 800
    height = 600

    logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO)

    pygame.init()

    pygame.display.set_caption('Blob World')
    game_display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    blue_blobs  = dict(enumerate([BlueBlob(width, height)  for _ in range(starting_blue_blobs)]))
    red_blobs   = dict(enumerate([RedBlob(width, height)   for _ in range(starting_red_blobs)]))
    green_blobs = dict(enumerate([GreenBlob(width, height) for _ in range(starting_green_blobs)]))

    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            blue_blobs, red_blobs, green_blobs = draw_environment(game_display, [blue_blobs, red_blobs, green_blobs])
            clock.tick(50)
        except Exception as e:
            logging.critical(str(e))
            running = False

    pygame.quit()
    quit()


if __name__ == '__main__':
    # blue_blobs  = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    # red_blobs   = dict(enumerate([RedBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    # green_blobs = dict(enumerate([GreenBlob(GREEN, WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    main()