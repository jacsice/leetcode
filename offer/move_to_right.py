class Solution(object):
    """
    数组中的数字向右移，最高位移到最低位
    （1，2，3，4，5） 移动两次 (4,5,1,2,3)
    O(n)
    """

    def move_to_right(self, arr, count):
        arr_len = len(arr)
        count %= arr_len
        left_move = (arr_len - count)
        right_move = count
        for i in range(left_move//2):
            arr[i], arr[left_move-1-i] = arr[left_move-1-i], arr[i]

        for i in range(right_move//2):
            arr[left_move+i], arr[arr_len-i-1] = arr[arr_len-i-1], arr[left_move+i]

        for i in range(arr_len//2):
            arr[i], arr[arr_len-i-1] = arr[arr_len-i-1], arr[i]

        return arr


if __name__ == '__main__':
    print(Solution().move_to_right([1, 2, 3, 4, 5, 6], 2))

from datetime import timedelta