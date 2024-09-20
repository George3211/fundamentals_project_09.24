print(f"Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice = input("Enter the number of your choice (1-4): ")

text = ''

if choice == '1':
    text = "Learning Python is fun!"

    if "Python" in text:
        print("Python")

    if text != "LEARNING PYTHON IS FUN!":
        text = "LEARNING PYTHON IS FUN!"
        print(text)

    if text != "Learning Python is great!":
        text = "Learning Python is great!"
        print(text)

elif choice == '2':

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print(f"Addition: {abs(num1 + num2)}")
    print(f"Subtraction: {abs(num1 - num2)}")
    print(f"Multiplication: {abs(num1 * num2)}")
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Division: {abs(num1 / num2)}")
    print(f"{num1} raised to the power of {num2} is: {num1 ** num2}")

elif choice == '3':

    is_python_fun = True
    is_sunny = False

    if not is_python_fun:
        print(f'Python is not fun!')
    elif not is_python_fun and is_sunny:
        print('Python is fun!')
    elif is_python_fun or is_sunny:
        print('Learning Python is fun!')

    if not is_python_fun and 10 > 5:
        print('Тen is greater than five')

    if is_sunny and 10 < 5:
        print('Five is greater than ten')

    if is_python_fun or not is_sunny or 10 == 10:
        print('Ten is draw ten')

    if is_python_fun and 10 >= 6:
        print('Ten is greater than six or draw six')

    if not is_sunny or 10 <= 6:
        print('Ten is not greater than six or draw six')

elif choice == '4':

    list_is = [17, 'George', True]

    if 18 not in list_is:
        list_is = [17, 'George', True, 18]
        print(list_is)

        print(list_is[-1])

    fruits_tuple = ('apple', 'banana', 'cherry')

    if len(fruits_tuple) > 0:
        print(len(fruits_tuple))

    if len(fruits_tuple) < 0:
        print('Congratulations!')
    else:
        print('TypeError!!!')

    dictionary_is = {'name': 'George',
                     'age': 17,
                     'city': 'Sofia'}

    print(17)

    if {'gender': 'male'} != dictionary_is:
        dictionary_is = {'name': 'George',
                         'age': 17,
                         'city': 'Sofia',
                         'gender': 'male'}
        print(dictionary_is)

else:
    print('Error: invalid choice!!!')
    print('Enter the new choice!')




