import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **data):
        self.contents = [k for k, v in data.items() for _ in range(v)]

    def draw(self, no_of_balls):
        return self.contents if no_of_balls > len(self.contents) else [self.contents.pop(random.randrange(len(self.contents))) for _ in range(no_of_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        ball_drawn = copy_hat.draw(num_balls_drawn)
        ball_req = sum([1 for k, v in expected_balls.items() if ball_drawn.count(k) >= v])
        m += 1 if ball_req == len(expected_balls) else 0
    return m/num_experiments


