cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0,1]
    if n == [0]:
        return([])
    elif n == 1:
        return([0])
    else:
        for _ in range(int(n)-2):
            fib.append(sum(fib[-2:]))
        return(fib)
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))