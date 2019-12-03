import datetime

import pygame

from document import Document
from screen_handler import ScreenHandler
from input_handler import InputHandler


class Main(object):
    """
    Main class for 08b15.
    """
    def __init__(self, size):
        """
        :param size: tuple
        """
        self.size = size
        self.running = True

        self.document = Document(self.size)
        self.screen_handler = ScreenHandler(self.size)
        self.input_handler = InputHandler()

        self.using_mode = 0
        pygame.display.set_mode(size)

    def run(self):
        """
        :return: None
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.input_handler.catch(event, self.screen_handler, self.document, self)

            self.update_screen()

    def update_screen(self):
        """
        :return: None
        """
        self.screen_handler.draw_screen(self.document, self.using_mode)
        pygame.display.update()

    def save_screen(self):
        """
        Saves screenshot into /screens
        :return: None
        """
        path = 'screens/output_%s.png' % str(datetime.datetime.now())[:-7].replace(":", ",")

        save_screen = pygame.Surface((self.screen_handler.size[0] * 2, self.screen_handler.size[1] * 2))

        save_screen.blit(self.screen_handler.screen, (0, 0))
        save_screen.blit(pygame.transform.flip(self.screen_handler.screen, 0, 1), (0, self.screen_handler.size[1]))
        save_screen.blit(pygame.transform.flip(self.screen_handler.screen, 1, 0), (self.screen_handler.size[0], 0))
        save_screen.blit(pygame.transform.flip(self.screen_handler.screen, 1, 1), (self.screen_handler.size[0],
                                                                                   self.screen_handler.size[1]))

        pygame.image.save(save_screen, path)


pygame.init()
X = Main((1000, 1000))
X.run()
