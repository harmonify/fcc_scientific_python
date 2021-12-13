# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
# https://replit.com/@harmonify/polygon-area-calculator#shape_calculator.py

from __future__ import annotations


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> int:
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        row = "*" * self.width
        return "".join(f"{row}\n" for _ in range(self.height))

    def get_amount_inside(self, shape: Rectangle):
        return (self.height // shape.height) * (self.width // shape.width)


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

    def set_width(self, width: int) -> None:
        self.set_side(width)

    def set_height(self, height: int) -> None:
        self.set_side(height)

    def set_side(self, side: int) -> None:
        self.width = side
        self.height = side


def main(args=None):
    # rectangle
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    # square
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    # test interoperability on get_amount_inside
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))


if __name__ == '__main__':
    main()
