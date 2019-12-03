import random


class Rect(object):
    """
    Rect objects.
    """
    def __init__(self, red, green, blue, x, y, shape, width, length, height, random_mode=0):
        """
        :param red: int
        :param green: int
        :param blue: int
        :param x: int
        :param y: int
        :param shape: int
        :param width: int
        :param length: int
        :param height: int
        :param random_mode: int
        """
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        self.shape = shape
        self.width = width
        self.length = length
        self.height = height

        self.random_mode = random_mode

    def draw_yourself(self, screen):
        """
        Draw Rect.
        :param screen: Screen object
        :return: None
        """
        old_red, old_green, old_blue = self.red, self.green, self.blue
        old_length, old_height = self.length, self.height

        random_table = {
            0: [],
            1: [self.randomize_colors],
            2: [self.randomize_extra],
            3: [self.randomize_colors, self.randomize_extra]
        }

        for randomize_function in random_table[self.random_mode]:
            randomize_function()

        shapes_table = {
            'RECT': 'screen.drawRec(self.red, self.green, self.blue, self.x, self.y, self.length, self.height, '
                    'self.width)',
            'CIRCLE': 'screen.drawCirc(self.red,self.green, self.blue, self.x,  self.y, self.length, self.width)',
            'LINES': 'screen.drawLine(self.red,self.green, self.blue, self.x,  self.y, self.length, self.height, '
                     'self.width)',
            'ELLIPSE': 'screen.drawEllipse(self.red,self.green, self.blue, self.x,  self.y, self.length, self.height, '
                       'self.width)',
            'TRIANGLE': 'screen.drawPolygon(self.red,self.green, self.blue, [(self.x, self.y), (self.x - self.length, '
                        'self.y + self.height), (self.x + self.length , self.y + self.height)], self.width)',
            'REC-TRIANGLE': 'screen.drawPolygon(self.red,self.green, self.blue, [(self.x, self.y), (self.x, self.y + '
                            'self.height), (self.x + self.length , self.y + self.height)], self.width)',
            'OBTUSE-TRIANGLE': 'screen.drawPolygon(self.red,self.green, self.blue, [(self.x, self.y), (self.x + '
                               'int(self.length/2), self.y + self.height), (self.x + self.length , self.y + '
                               'self.height)], self.width)',
            'PENTAGON': 'screen.drawPolygon(self.red,self.green,self.blue, [(self.x, self.y), (self.x - self.length, '
                        'self.y + int(self.height/3)), (self.x - int(self.length/2), self.y + self.height), (self.x + '
                        'int(self.length/2), self.y + self.height), (self.x + self.length , self.y + '
                        'int(self.height/3))], self.width)',
            'HEXAGON': 'screen.drawPolygon(self.red, self.green, self.blue, [(self.x, self.y), (self.x - '
                       'int(self.length * 0.5), self.y + int(self.height/2)), (self.x,  self.y + self.height), (self.x '
                       '+ self.length, self.y + self.height), (self.x + int(self.length * 1.5), self.y + '
                       'int(self.height/2)), (self.x + self.length,self.y)], self.width)',
            'NONE': 'None'}

        exec(shapes_table[self.shape])

        self.red, self.green, self.blue = old_red, old_green, old_blue
        self.length, self.height = old_length, old_height

    def toggle_random_mode(self):
        """
        :return: None
        """
        self.random_mode = (self.random_mode + 1) % 4

    def randomize_colors(self):
        """
        :return: None
        """
        self.red = random.randrange(0, self.red)
        self.green = random.randrange(0, self.green)
        self.blue = random.randrange(0, self.blue)

    def randomize_extra(self):
        """
        :return: None
        """
        self.length = random.randrange(0, self.length)
        self.height = random.randrange(0, self.height)

    def edit(self, var, amount):
        """
        Edit rect.
        :param var: str
        :param amount: int
        :return: None
        """

        # Variable table
        var_table = {
            'r': {'attr_name': 'red', 'max': 255, 'min': 1},
            'b': {'attr_name': 'blue', 'max': 255, 'min': 1},
            'g': {'attr_name': 'green', 'max': 255, 'min': 1},
            'x': {'attr_name': 'x', 'max': 99999999999, 'min': 0},
            'y': {'attr_name': 'y', 'max': 99999999999, 'min': 0},
            'w': {'attr_name': 'width', 'max': 99999999999, 'min': 0},
            'q': {'attr_name': 'length', 'max': 99999999999, 'min': 2},
            'e': {'attr_name': 'height', 'max': 99999999999, 'min': 2}
        }

        if var_table.get(var):
            var_table_option = var_table[var]

            # Constrict value
            new_value = (getattr(self, var_table_option['attr_name']) + amount)
            new_value = var_table_option['max'] if new_value > var_table_option['max'] else new_value
            new_value = var_table_option['min'] if new_value < var_table_option['min'] else new_value

            # Set value
            setattr(self, var_table_option['attr_name'], new_value)
        else:
            print("INVALID EDIT KEY: %s" % var)  # TODO: REMOVE, ONLY FOR DEBUG
