"""
https://www.hackerrank.com/challenges/nested-list/problem
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry

Constraints: 2<=N<=5
There will always be one or more students having the second lowest grade.
Print names alphabetically.
"""
if __name__ == '__main__':
    scores = [] #initialize scores

    for _ in range(int(input())): #number of names to be entered by user (N)
        # name = input() #automatically a string
        # score = float(input())
        # scores.append(name,score) #append only takes one argument. Need to get as list first.
        scores.append([input(),float(input())]) #this works and is more pythonic.

    #print(scores)

    penultimate = sorted(list(set(score for name, score in scores)))[1]#turn to set, then back to list, then sort, then second value.
    # print(type(penultimate)) # it is a float!

    """
    for a,b in sorted(scores):
         if b == penultimate:
             print (a)
    """
    #more pythonic:
    print('\n'.join([a for a,b in sorted(scores) if b == penultimate])) #if score = penult score, print associated name (a). sorted() for alphabetically
