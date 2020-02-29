# 旋转数组的最小数字


def min_rotate_arr(arr):
    left = 0
    right = len(arr) - 1
    if arr[left] < arr[right]:
        return 0
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[left]:
            if arr[mid] > arr[mid+1]:
                return mid + 1
            left = mid
        elif arr[mid] == arr[left]:
            right -= 1
        else:
            if arr[mid-1] > arr[mid]:
                return mid
            right = mid
    return left


if __name__ == '__main__':
    print(min_rotate_arr([1,2,3,4,5,0]))