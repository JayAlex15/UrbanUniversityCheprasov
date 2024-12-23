from math import sqrt

Pi = 3.14

class Figure:
    sides_count = 0
    filled = True

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides

    def get_color(self):
        figure_color = []
        for i in self.__color:
            figure_color.append(i)
        return figure_color

    def __is_valid_color(self, color):
        rgb_flag = True
        for i in color:
            if i < 0 or i > 255:
                rgb_flag = False
                break
        return rgb_flag

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, *new_sides):
        figure_sides = []
        for i in new_sides:
            figure_sides.append(i)
        count_sides = 0
        side_flag = True
        for side in figure_sides:
            count_sides += 1
            if side <= 0:
                side_flag = False
            if count_sides != self.sides_count:
                side_flag = False
        return side_flag

    def get_sides(self):
        figure_sides = list(self.__sides)
        return figure_sides

    def __len__(self):
        figure_sides = self.get_sides()
        perimetr = sum(figure_sides)
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def circle_radius(self, *sides):
        curcle_side = self.get_sides()
        radius = curcle_side[0] / (2 * Pi)

    def get_square(self):
        circle_square = Pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_square(self):
        tri_sides = self.get_sides()
        p = sum(tri_sides) / 2
        p1 = p - tri_sides[0]
        p2 = p - tri_sides[1]
        p3 = p - tri_sides[2]
        s = sqrt(p * p1 * p2 * p3)
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color,*sides*12)

    def get_volume(self):
        sides = self.get_sides()
        volume = sides[0] ** 3
        return volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
