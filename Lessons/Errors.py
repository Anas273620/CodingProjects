# Error Handling


while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than zero')
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')


# def sum(num1, num2):
#     try:
#        return num1 + num2
#     except TypeError as err:
#         print(f'Please enter numbers {err}')

# print(sum(1, '2'))