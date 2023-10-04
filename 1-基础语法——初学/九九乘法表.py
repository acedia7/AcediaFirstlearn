for i in range(1,10):
    for j in range(1,10):
        print("{}*{}={:<6}".format(i,j,i*j),end="")
        if(j==9):
            print("\n")
            break