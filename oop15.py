class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def get_input(self):
        self._x=int(input('Please enter integer value for x: '))
        self._y=int(input('Please enter integer value for y: '))

    def dist_to_point(self, other):
        'Compute the Euclidean distance between two Point objects'
        delta_x = self._x - other._x
        delta_y = self._y - other._y
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    def display(self):
        print("value of x: ",self._x)
        print("value of y: ",self._y)
run = Point()
run.get_input()
run.dist_to_point()
