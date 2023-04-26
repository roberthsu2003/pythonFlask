def outer_function():
    x = 1
    def inner_function():
        nonlocal x       
        print(x)
        x = x + 1

    return inner_function


f = outer_function()
f()