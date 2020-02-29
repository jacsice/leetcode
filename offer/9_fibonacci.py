# 菲波那切数列

f_dict = {}


def fibonacci(num):
    if num in [0, 1]:
        return num
    total = fibonacci(num-1) + fibonacci(num-2)
    if num in f_dict:
        return f_dict.get(num)
    f_dict[num] = total
    print("=========", num)
    return total


def frog(count):
    if count in (1, 0):
        return 1
    return frog(count-1) + frog(count-2)


if __name__ == '__main__':
    print(frog(3))