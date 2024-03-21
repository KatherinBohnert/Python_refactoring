def input_evaluation():
    while True:
        print('Please enter your rating from 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Please enter a number from 1 to 5')
            else:
                print('Please enter your comment')
                comment = input()
                post = f'ポイント: {point} コメント: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Please enter your rating points in numbers.')

def show_results():
    print('Results so far')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

while True:
    print('Please select the process you want to perform')
    print('1: Enter evaluation points and comments')
    print('2: Check the results so far')
    print('3: End')
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            input_evaluation()
        elif num == 2:
            show_results()
        elif num == 3:
            print('Exit')
            break
        else:
            print('Please enter a number from 1 to 3')
    else:
        print('Please enter a number from 1 to 3')