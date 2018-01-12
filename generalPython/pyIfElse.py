if __name__ == '__main__':
    n = int(input())

    if n%2 != 0:
        print("Weird")
    elif (n%2 == 0 and (n < 6 or n > 20)):
        print("Not Weird")
    else:
        print("Weird")
