import math

def draw_lake(area=9, shape="square"):
    if(shape=="square"):
        n = int(math.sqrt(area))
        print(" " + n*"-")
        for i in range(n):
            print("|" + n*" " + "|")
        print(" " + n * "-")
    else:
        print("Sorry, now the shape should be square.")
    return
