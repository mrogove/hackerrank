"""
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ 10.

Sample Input

Guido
Rossum

Sample Output

Hello Guido Rossum! You just delved into python.

"""
def print_full_name(a, b):
    print("Hello "+a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
