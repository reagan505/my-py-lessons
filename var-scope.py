#local scope

#Enclosed scope example
def enclose_scope():
    x = 10  # Outer scope variable

    def nested_scope():
        nonlocal x  # Refers to the 'x' in the enclosing 'enclose_scope' function
        x = 20
        print(f"Inside nested_scope, x = {x}")

    nested_scope()  # Call the nested function
    print(f"After nested_scope, x = {x}")  # Now the value of 'x' should be modified to 20

# Call the outer function
enclose_scope()
