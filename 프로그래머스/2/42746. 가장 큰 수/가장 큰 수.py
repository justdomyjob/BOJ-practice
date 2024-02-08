def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = change, reverse= True)
    return str(int("".join(numbers)))
                   
def change(number):
    number = number*4
    number = number[:4]
    return number              
                   
     