#!/usr/bin/env python
#! -*- coding=utf-8 -*-

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 

分三次旋转
前半部分[4,3,2,1,5,6,7]
后半部分[4,3,2,1,7,6,5]
整体[5,6,7,1,2,3,4]
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, arr, k):
        arr_length = len(arr)
        k = k % arr_length
        self.reverse_arr(arr, 0, arr_length-k-1)
        self.reverse_arr(arr, arr_length-k, len(arr)-1)
        self.reverse_arr(arr, 0, len(arr)-1)
    
    def reverse_arr(self,arr, start, end):
        count = (end - start + 1)/2
        for i in range(count):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
