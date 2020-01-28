def draw_road(length=10, axis="horizontal"):
    if axis == "horizontal":
        for i in range(length):
            print("=")
    else:
        for i in range(length):
            print("||")
    return
