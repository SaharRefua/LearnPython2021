
def ModBooleanVector(array,x):
    booleanVector = []
    for item in array:
        item_as_int=int(item)
        if int(item_as_int) % x == 0:
            booleanVector.append(True)
        else:
            booleanVector.append(False)
    print(booleanVector)
#[1,2,3,4,5,6,7,8,9]
array=input("Please insert your Array:\n")
x=int(input("Please insert your X:\n"))

ModBooleanVector(array,x)



import numpy

def myDictConst(myKey, myVal):
    myDict = {
        myKey[1]: myVal[1],
        myKey[0]: myVal[0],
    }
    for i in range(len(myKey)-2):
        myDict[myKey[i+2]] = myVal[i+2]
    return myDict

def countMyStrings(myStr):
    myStr = myStr.lower()
    counts = {}
    for word in myStr.split(" "):
        if word not in counts.keys():
            counts[word] = 0
        counts[word] += 1

    return counts

# def myArange(*args):
#     print(args)
#     len(args)
#     # find number of argument of the function -> arg
#     ndarray=[];
#     if len(args)==1:
#         for i in range(0,a):
#             ndarray[i]= i
#     if len(args) == 2:
#         for i in range(a, b):
#             ndarray[i] = i
#     if len(args) == 3:
#         pass…


# Hurdle 4

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()



















    # Maze FIanl project


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         # move()
#         turn_right()
#     # if wall_in_front():
#     # jump()
#     if front_is_clear():
#         move()
#     else:
#         turn_left()



