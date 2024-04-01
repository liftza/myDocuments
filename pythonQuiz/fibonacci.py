def fibonacci(input):
    start = [0, 1]

    while start[-1] + start[-2] <= input:
        nextFn = start[-1] + start[-2]
        start.append(nextFn)

    return start


input = int(input("Enter numbers:"))
final = fibonacci(input)
print("Fibonacci your input:", input, "result :", final)