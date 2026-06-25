# main.py

print("--- Python Object Model: Mutable vs. Immutable Types ---")
print("\nUnderstanding how Python handles objects and references is key to knowing why your code behaves the way it does.")

# 1. Immutable Types (e.g., integers, strings, tuples)
# When you "change" an immutable object, you're actually creating a new object and reassigning the variable.
print("\n--- 1. Immutable Types (Integers) ---")
a = 10
b = a # b now refers to the same integer object as a
print(f"Initial: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")

a = 20 # Here, 'a' is reassigned to a NEW integer object. 'b' still refers to the old one.
print(f"After a = 20: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")
# Notice: id(a) changed, but id(b) remained the same as the original id(a).
# This shows that 'a' now points to a different object, while 'b' is untouched.

# 2. Mutable Types (e.g., lists, dictionaries, sets)
# When you modify a mutable object, the object itself changes, and all variables referencing it will see the change.
print("\n--- 2. Mutable Types (Lists) ---")
list1 = [1, 2, 3]
list2 = list1 # list2 now refers to the SAME list object as list1
print(f"Initial: list1 = {list1} (id: {id(list1)}), list2 = {list2} (id: {id(list2)})")
# Notice: Both list1 and list2 have the same object ID. They are names for the same underlying list.

list1.append(4) # Modifying the list object IN-PLACE via list1
print(f"After list1.append(4): list1 = {list1} (id: {id(list1)}), list2 = {list2} (id: {id(list2)})")
# Notice: Both list1 and list2 show the change, and their IDs are still the same.
# This is a common source of "magic" or unexpected behavior if not understood.
# The object itself was modified, not just a variable's reference.

# 3. Copying Mutable Objects (to avoid shared references)
print("\n--- 3. Shallow Copying Mutable Objects ---")
original_list = [10, 20, 30]
# To create an independent copy, you need to explicitly copy the object.
# For simple lists, slicing `[:]` or `list()` constructor creates a shallow copy.
copied_list = original_list[:] # Creates a new list object with the same elements
print(f"Initial: original_list = {original_list} (id: {id(original_list)})")
print(f"         copied_list = {copied_list} (id: {id(copied_list)})")
# Notice: The IDs are different. They are now two separate list objects.

original_list.append(40) # Modifying original_list
print(f"After original_list.append(40): original_list = {original_list} (id: {id(original_list)})")
print(f"                                copied_list = {copied_list} (id: {id(copied_list)})")
# Notice: Only original_list changed. copied_list remains independent.

# 4. Function Arguments and Mutability
print("\n--- 4. Function Arguments and Mutability ---")

def modify_list_in_function(my_list_param):
    # my_list_param is a reference to the same list object passed in
    print(f"  Inside function (before modification): {my_list_param} (id: {id(my_list_param)})")
    my_list_param.append("modified") # Modifies the original list object
    print(f"  Inside function (after modification): {my_list_param} (id: {id(my_list_param)})")

my_data = ["item1", "item2"]
print(f"Before function call: {my_data} (id: {id(my_data)})")
modify_list_in_function(my_data)
print(f"After function call: {my_data} (id: {id(my_data)})")
# Notice: The 'my_data' list outside the function was permanently modified.
# This happens because Python passes arguments by object reference.

def try_to_change_immutable_in_function(my_int_param):
    print(f"  Inside function (before modification): {my_int_param} (id: {id(my_int_param)})")
    my_int_param = 99 # This creates a NEW integer object and reassigns my_int_param locally
    print(f"  Inside function (after modification): {my_int_param} (id: {id(my_int_param)})")

my_number = 10
print(f"\nBefore function call (immutable): {my_number} (id: {id(my_number)})")
try_to_change_immutable_in_function(my_number)
print(f"After function call (immutable): {my_number} (id: {id(my_number)})")
# Notice: 'my_number' outside the function remains unchanged.
# The reassignment inside the function only affected the local parameter.

print("\n--- Conclusion ---")
print("Python variables are names (references) that point to objects in memory.")
print("Understanding whether an object is mutable (can be changed in-place) or immutable (creates a new object upon 'change')")
print("is fundamental to predicting how your code will behave, especially when passing objects to functions or assigning variables.")
