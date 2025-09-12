def show_numbers(N):
    for i in range(N + 1):  # loop from 0 to N
        if i % 2 == 0:
            print(f"{i} Even")
        else:
            print(f"{i} Odd")
show_numbers(10)
