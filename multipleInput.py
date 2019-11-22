x , y = input("Enter two values: ").split()
print("First value {} and second value {}".format(x,y))

x = list(map(int, input("Enter multiple values : ").split()))
print("List of values : ", x)

x , y = [int(x) for x in input("Enter two value: ").split()]
print("First value {} and second value {}".format(x,y))

x = [int(x) for x in input("Enter multiple values : ").split()]
print("Multiple value : ",x)
