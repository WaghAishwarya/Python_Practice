def evennood(x):
    countev = 0
    countod = 0
    for i in x:
        if i%2==0:
            print('even')
            countev+=1

        else:
            print('odd')
            countod+=1

    print('even no count', countev)
    print('odd no count', countod)
x = [1,2,3,4,5,6,7,8]
evennood(x)