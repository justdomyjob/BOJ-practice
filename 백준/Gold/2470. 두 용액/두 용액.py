import sys

n = int(input())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))

numbers.sort()

start = 0
end = n-1
solution = []
while start < end:
    if numbers[start] + numbers[end] < 0:
        solution.append((abs(numbers[start] + numbers[end]), numbers[start], numbers[end]))
        start+=1
    elif numbers[start] + numbers[end] > 0:
        solution.append((abs(numbers[start] + numbers[end]), numbers[start], numbers[end]))
        end -= 1
    else:
        print(numbers[start],numbers[end])
        exit(0)
solution.sort()
print(solution[0][1],solution[0][2])
