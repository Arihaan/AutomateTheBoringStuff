def comma_code(arr):
    if not arr:
        print("Empty List!")
    elif len(arr) == 1:
        print(arr[0])
    else:
        out_str = ''
        for i in range(len(arr)):
            if i == len(arr) - 1:
                out_str += 'and ' + arr[i]
            else:
                out_str += arr[i] + ", "
        print(out_str)


spam = ['apples', 'bananas', 'tofu', 'cats']  # test array

comma_code(spam)
