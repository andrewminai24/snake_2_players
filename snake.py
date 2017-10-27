class Snake:

    def __init__(self, positionX, positionY, bodyX1, bodyY1, bodyX2, bodyY2):
        self.position = [positionX, positionY]
        self.body = [[self.position[0], self.position[1]], [bodyX1, bodyY1], [bodyX2, bodyY2]]
        self.score = 0

    def inBounds(self):
        if self.position[0] < 0 or self.position[0] > 720 or self.position[1] < 0 or self.position[1] > 480:
            return False

        return True

    def update(self, direction):
        if direction == 'RIGHT':
            self.position[0] += 10
        elif direction == 'LEFT':
            self.position[0] -= 10
        elif direction == 'UP':
            self.position[1] -= 10
        elif direction == 'DOWN':
            self.position[1] += 10