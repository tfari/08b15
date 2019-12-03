import pygame


class InputHandler(object):
    """
    Class for handling events.
    """
    def __init__(self):
        self.modding = False
        self.modding_type = -1
        self.last_key = ''

        self.mouse_mode = -1

    def catch(self, event, screen_handler, document, callback):
        """
        Catch events.
        :param event: pygame.event object being passed through
        :param screen_handler: ScreenHandler object
        :param document: Document object
        :param callback: Main object
        :return: None
        """

        input_table = {
            '1': 'document.mouse_rect.shape = "LINES"',
            '2': 'document.mouse_rect.shape = "CIRCLE"',
            '3': 'document.mouse_rect.shape = "RECT"',
            '4': 'document.mouse_rect.shape = "ELLIPSE"',
            '5': 'document.mouse_rect.shape = "TRIANGLE"',
            '6': 'document.mouse_rect.shape = "REC-TRIANGLE"',
            '7': 'document.mouse_rect.shape = "OBTUSE-TRIANGLE"',
            '8': 'document.mouse_rect.shape = "PENTAGON"',
            '9': 'document.mouse_rect.shape = "HEXAGON"',
            '0': 'document.mouse_rect.shape = "NONE"',

            'up': 'self.modding = True; self.modding_type = 1',
            'down': 'self.modding = True; self.modding_type = -1',
            'escape': 'document.reset_rects()',

            's': 'callback.save_screen()',
            'a': 'pass',

            'left_shift': 'callback.using_mode = 1',
            'right_shift': 'callback.using_mode = 0',

            #
            'z': 'screen_handler.toggle_reflection_mode()',
            'tab': 'self.toggle_mouse_mode()',

        }


        #

        if event.type == pygame.MOUSEMOTION:
            if self.mouse_mode == 1:
                document.add_rect(document.mouse_rect)

            document.mouse_rect.x, document.mouse_rect.y = event.pos[0], event.pos[1]

        elif event.type == pygame.KEYDOWN:
            key = str(pygame.key.name(event.key))

            # exec(input_table[key])  # TODO: REMOVE, ONLY FOR DEBUGGING

            try:
                exec(input_table[key])
            except Exception as e:
                print("ERROR WITH KEY: %s" % key)  # TODO: REMOVE, ONLY FOR DEBUGGING
                self.last_key = key

        elif event.type == pygame.KEYUP:
            key = str(pygame.key.name(event.key))

            if key == 'down' or key == 'up':
                self.last_key = ''
                self.modding = False

        elif event.type == pygame.MOUSEBUTTONUP:
            # LEFT CLICK CREATES NEW RECT
            if event.button == 1:
                document.add_rect(document.mouse_rect)

        self.mod_run(document)

    def mod_run(self, document):
        """
        Modify values by holding keys.
        :param document: Document object
        :return: None
        """
        if self.modding:
            document.mouse_rect.edit(self.last_key, self.modding_type)

    def toggle_mouse_mode(self):
        """
        :return: None
        """
        self.mouse_mode *= -1
