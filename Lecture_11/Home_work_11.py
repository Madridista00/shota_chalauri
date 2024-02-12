# <!-- მოცემულია რიცხვების სია `[94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]`

# გამოიყენეთ სორტირების ალორითმები: `bubble sort`, `merge sort` და `insertion sort`.

# შედეგები დაბეჭდეთ ეკრანზე. -->


## ===BUBBLE_SORT===

# def bubble_sort(arr):
#     n = len(arr)

#     for k in range(n-1, 0, -1):
#         for m in range(k):
#             if arr[m] > arr[m + 1]:
#                 arr[m], arr[m + 1] = arr[m + 1], arr[m]


# #=========================
                
# list = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# bubble_sort(list)

# print("BUBBLE_SORT for list is:")
# print(list)



## ===MERGE_SORT===

# def merge_sort(arr):
#     n = len(arr)
#     middle = n // 2

#     if n <= 1:
#         return arr
    

#     left = merge_sort(arr[:middle])
#     right = merge_sort(arr[middle:])

#     return merge_two_list(left, right)

# def merge_two_list(a, b):
#     c = []
#     i = j = 0

#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     c += a[i:] + b[j:]

#     return c



# #=============================
# list = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

# print("MERGE_SORT for list is:")
# print(merge_sort(list))



## ===INSERTION_SORT===

# def inspection_sort(arr):
#     n = len(arr)

#     for i in range(1, n):
#         j= i

#         while j > 0 and arr[j] < arr[j - 1]:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]

#             j-= 1


# #========================
# list = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# inspection_sort(list)

# print("INSPECTION_SORT for list is:")
# print(list)





