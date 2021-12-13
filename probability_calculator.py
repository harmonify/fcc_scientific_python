# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
# https://replit.com/@harmonify/probability-calculator#prob_calculator.py

import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for ball, count in kwargs.items():
            self.contents.extend([ball for _ in range(count)])

    def draw(self, n: int) -> list[str]:
        if n >= len(self.contents):
            result = copy.copy(self.contents)
            self.contents.clear()
            return result

        return [self.contents.pop(random.randrange(
                0, len(self.contents))) for _ in range(n)]


def experiment(hat: Hat, expected_balls: dict[str, int],
               num_balls_drawn: int, num_experiments: int) -> float:
    m = 0
    for _ in range(num_experiments):
        result = Counter(copy.deepcopy(hat).draw(num_balls_drawn))
        conditions = [count <= result.get(ball, 0)
                      for ball, count in expected_balls.items()]

        if all(conditions) is True:
            m += 1

    return m / num_experiments


def main(args=None):
    # set up
    hat = Hat(black=6, red=4, green=3)

    # find probability of getting red >= 2 and green >= 1
    probability = experiment(hat=hat,
                             expected_balls={"red": 2, "green": 1},
                             num_balls_drawn=5,
                             num_experiments=2000)

    print(probability)


if __name__ == '__main__':
    main()
