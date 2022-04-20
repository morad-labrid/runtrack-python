nbr = int(input("enter number"))
space = " "
slashL = "/"
slashR = "\\"
for x in range(nbr):
    left = space*(nbr-x)+slashL
    center = x*2*" "
    underscore = x*2*"_"
    right = slashR+space*(nbr-x)
    if x == nbr-1:
        print(left+underscore+right)
    else:
        print(left+center+right)
