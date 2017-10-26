class Snake:

    def __init__(self, positionX, positionY, bodyX, bodyY):
        self.position = [positionX, positionY]
        self.body = [[self.position[0], self.position[1]], [bodyX, bodyY], [bodyX - 10, bodyY - 10]]

    def inBounds(self):
        if self.position[0] < 0 or self.position[1] > 720 or self.position[1] < 0 or self.position[1] > 480:
            return True

        return False