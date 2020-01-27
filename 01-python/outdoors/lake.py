def draw_lake(area=1, shape="square", width=1, length=1):
    """
    Print a lake

    Parameters:
        area(int): Area of the lake
        shape(string): Shape of the lake
        width(int): Width of the lake
        length(int): length of the lake

    The shape of lake should be square or rectangle.
    If the lake is square, the area should be a square number.
    If the lake is rectangle, the given width and length should compatible with the area.
    """
    if shape == "square":
        n = get_perfect_square_root(area)
        print(" " + n*"-")
        for i in range(n):
            print("|" + n*" " + "|")
        print(" " + n * "-")
        return
    if shape == "rectangle":
        if width*length != area:
            raise Exception("width and length are wrong!")
        else:
            print(" " + length * "-")
            for i in range(width):
                print("|" + length * " " + "|")
            print(" " + length * "-")
            return
    raise Exception("Sorry, now the shape should be square or rectangle.")


def get_perfect_square_root(n):
    i = 1
    while i * i <= n:
        if (n % i == 0) and (n / i == i):
            return i
        i = i + 1
    raise ValueError("area is not a perfect square")
