point = {'x':4,'y':-5}
print("{x} {y}".format(**point))

print("{x} {y}".format_map(point))

class Coordinate(dict):
    def __missing__(self,key):
        return key

print("{x}, {y}".format_map(Coordinate(x='6')))
print("{x}, {y}".format_map(Coordinate(y = '5')))
print("{x}, {y}".format_map(Coordinate(x = '6', y = '5')))
