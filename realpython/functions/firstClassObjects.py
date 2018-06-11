def foo(bar):
    return bar + 1


print('first')
print(foo)

print('second')
print(foo(2))

print('third')
print(type(foo))


# foo function is being passed as a parameter.
def call_foo_with_arg(foo, arg):
    return foo(arg)


print('fourth')
print(call_foo_with_arg(foo, 3))
