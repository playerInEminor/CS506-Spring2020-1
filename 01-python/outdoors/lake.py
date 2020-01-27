import math

def draw_lake(area=1, shape="square"):
    if(shape=="square"):
        for i in range(math.sqrt(area)):
            print("-")
        for i in range(math.sqrt(area)):
            print("|" + math.sqrt(area)*" " + "|")
        for i in range(math.sqrt(area)):
            print("-")
    # n =math.sqrt(area) - 1
    # if(shape=="triangle"):
    #     for i in range(1, area + 1):
    #         print(math.sqrt(area) - 1）i*"*")
    return