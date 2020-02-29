# 数字转为2进制后，1 的个数


def one_in_binary(num):
    count = 0
    while num != 0:
        if num != (num >> 1) << 1:
            count += 1
        num = num >> 1
    return count


if __name__ == '__main__':
    print(one_in_binary(8))