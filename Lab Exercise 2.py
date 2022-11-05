list1 = [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]

print("1 -> Add an element")
print("2 -> Insert an element")
print("3 -> Modify an element")
print("4 -> Delete an element")
print("5 -> Arrange in ascending order")
print("6 -> Arrange in descending order")

while True:
    choice = input("\nWhat do you want to do? (1-6): ")

    if choice == '1':
        append_element = int(input("Enter the element you want to add: "))
        list1.append(append_element)
        print("The element has been added")
        print("This is the new array:", list1)

    elif choice == '2':
        insert_index = int(input("Enter the index, where you want to place your element: "))
        insert_element = int(input("Enter the element you want to insert: "))
        list1.insert(insert_index, insert_element)
        print("The element has been added")
        print("This is the new array:", list1)

    elif choice == '3':
        modify_index = int(input("Enter the index of the element you want to modify: "))
        modify_element = int(input("Enter the element you want to include: "))
        list1[modify_index] = modify_element
        print("This is the new array:", list1)

    elif choice == '4':
        delete_index = int(input("Enter the index you want to delete: "))
        list1.pop(delete_index)
        print("This is the new array:", list1)

    elif choice == '5':
        list1.sort()
        print("The array has been arranged to ascending order")
        print("This is the new array:", list1)

    elif choice == '6':
        list1.sort()
        list1.reverse()
        print("The array has been arranged to descending order")
        print("This is the new array:", list1)


try_again = input("Do you want to continue? (Yes/No):")
if try_again == "Yes":
    continue

    while try_again not in ("Yes", "yes", "No", "no"):
            try_again = input("Do you want to try again?(Yes/No): ")
            if try_again == "No":
                break