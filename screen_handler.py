import pygame


class ScreenHandler(object):
    """
    Object that handles screen.
    """
    def __init__(self, size):
        """
        :param size: tuple
        """
        self.myfont = pygame.font.SysFont('monospace', 12)
        self.size = size
        self.display_screen = pygame.display.set_caption('08b15')
        self.screen = pygame.Surface(self.size)

        self.reflection_mode = 1

        self.resize_screen(size)

    def toggle_reflection_mode(self):
        """
        :return: None
        """
        self.reflection_mode *= -1

    def resize_screen(self, size):
        """
        :param size: tuple
        :return: None
        """
        self.display_screen = pygame.display.set_mode(size)

    def clean_screen(self):
        """
        :return: None
        """
        self.drawRec(1, 1, 1, 0, 0, self.size[0], self.size[1], 0)

    def draw_screen(self, document, using_mode):
        """
        :param document: Document object
        :param using_mode: int
        :return: None
        """

        self.clean_screen()

        # Show mouse_rect
        if using_mode == 0:
            document.mouse_rect.draw_yourself(self)

        # Draw rects
        for rect in document.rect_list:
            rect.draw_yourself(self)

        # Reflection mode
        if self.reflection_mode == 1:
            self.reflect_screen()
        else:
            self.partial_screen()

        self.draw_infobar(document)

    def partial_screen(self):
        """
        :return: None
        """
        self.display_screen.blit(self.screen, (0, 0))

    def reflect_screen(self):
        """
        :return: None
        """
        parts = [pygame.transform.scale(self.screen, (int(self.size[0] / 2), int(self.size[1] / 2))),
                 pygame.transform.flip(pygame.transform.scale(self.screen, (int(self.size[0] / 2), int(self.size[1] / 2)
                                                                           )), 1, 0),
                 pygame.transform.flip(pygame.transform.scale(self.screen, (int(self.size[0] / 2), int(self.size[1] / 2)
                                                                           )), 0, 1),
                 pygame.transform.flip(pygame.transform.scale(self.screen, (int(self.size[0] / 2), int(self.size[1] / 2)
                                                                           )), 1, 1)]
        self.display_screen.blit(parts[0], (0, 0))
        self.display_screen.blit(parts[1], (self.size[0]/2, 0))
        self.display_screen.blit(parts[2], (0, self.size[1]/2))
        self.display_screen.blit(parts[3], (self.size[0]/2, self.size[1]/2))

    def draw_infobar(self, document):
        """
        :param document: Document object
        :return: None
        """
        self.drawRec(1, 1, 1, 0, 0, document.size[0], 25, 0)

        line = ("R: " + str(document.mouse_rect.red) + " | " + "G: " + str(document.mouse_rect.green) + " | " + "B: " +
                str(document.mouse_rect.blue) + " | " + "X: " + str(document.mouse_rect.x) + " | " + "Y"
                + str(document.mouse_rect.y) + " | " + "Q: " + str(document.mouse_rect.length) + " | " + "E"
                + str(document.mouse_rect.height) + " | " + "W: " + str(document.mouse_rect.width) + " | " + "SHAPE: "
                + str(document.mouse_rect.shape) + ' | ' + " RMODE: " + str(document.mouse_rect.random_mode) + " | " +
                "RECS: " + str(len(document.rect_list)))

        label = self.myfont.render(line, 1, (255, 255, 255))

        self.display_screen.blit(label, (0, 0))

    """
    
    """
    def drawRec(self, r, g, b, start, top, length, height, width):
        pygame.draw.rect(self.screen, (r, g, b), (start, top, length, height), width)

    def drawCirc(self, r, g, b, location_x, location_y, circumference, width):
        pygame.draw.circle(self.screen, (r, g, b), (location_x, location_y), circumference + width, width)

    def drawLine(self, r, g, b, location_x, location_y, CHANGE_X, CHANGE_Y, width):
        pygame.draw.line(self.screen, (r, g, b), (location_x, location_y), (CHANGE_X, CHANGE_Y), width)

    def drawEllipse(self, r, g, b, location_x, location_y, height, length, width):
        pygame.draw.ellipse(self.screen, (r, g, b), (location_x, location_y, length, height), width)

    def drawPolygon(self, r, g, b, location_list, width):
        pygame.draw.polygon(self.screen, (r, g, b), location_list, width)
