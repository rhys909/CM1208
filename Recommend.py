import numpy as np
from itertools import zip_longest

def read_history():
    #Reads the history file and generates a list
    hist_file = open("history.txt", "r")
    hist_content = hist_file.read().split()
    No_Customers = hist_content[0]
    No_Items = hist_content[1]
    No_Trans = hist_content[2]
    hist_content.pop(0)
    hist_content.pop(0)
    hist_content.pop(0)
    hist_file.close()

    return hist_content

def read_cart():
    cart_file = open("queries.txt", "r")
    cart_content = cart_file.readlines()
    cart_list = [i.strip() for i in cart_content]
    return cart_list

def calculate_angle():
    hist = read_history()
    cart_query = read_cart()
    temp_list = []
    count = 0
    print(cart_query[0])
    for i in range(len(hist)):
        t = hist[i]
        if t == cart_query[0]:
            count += 1
        else:
            temp_list.append(hist[i])

    temp_list = np.array(temp_list, dtype=float)
    print(angle(temp_list,[2,0,0,0,0,0,0,0]))
    print(temp_list)

def entries():
    hist_list = read_history()
    count = 0
    for i in hist_list:
        hist_list[]
    print(count)

def cart_calculator():
    hist_list = read_history()
    cart_list = read_cart()


hist_list = read_history()
print(hist_list)
cart_list = read_cart()
print(cart_list)
entries()
calculate_angle()
