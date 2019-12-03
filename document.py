from rect import Rect


class Document(object):
    """
    Class that holds the elements being drawn.
    """
    def __init__(self, size):
        """
        :param size: tuple
        """
        self.size = size
        self.rect_list = []
        self.mouse_rect = Rect(1, 132, 255, 0, 0, 'LINES', 1, 300, 300)  # First rect.

    def add_rect(self, other_rect):
        """
        Add rect to the rect_list by copying the rect object passed
        :param other_rect: Rect object to copy contents from
        :return: None
        """
        new_rect = Rect(other_rect.red, other_rect.green, other_rect.blue, other_rect.x, other_rect.y, other_rect.shape,
                        other_rect.width, other_rect.length, other_rect.height, other_rect.random_mode)

        self.rect_list.append(new_rect)

    def reset_rects(self):
        """
        :return: None
        """
        self.rect_list = []