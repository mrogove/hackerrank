"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem

2<=n<=10
0<=marks<=100 (can be float)

print average of marks obtained by particular student. 2 decimals.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() #user determines student we care about
    query_scores = student_marks[query_name] #that student's scores

    print("{0:0.2f}".format(sum(query_scores)/(len(query_scores)))) #compute mean

    #assumes already formatted as string - use str.format for float formatting :/
