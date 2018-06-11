def parent():
    print("Printing from the parent() function")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())


# when called the first and second child functions are called
# can't call nested functions outside of the scope which is inside the parent function
parent()
