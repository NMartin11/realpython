def my_decorator(some_functions):

    def wrapper():

        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_functions()

        print("Something is happening after some_functions() is called.")

    return wrapper

if __name__ == "__main__":
    my_decorator()

