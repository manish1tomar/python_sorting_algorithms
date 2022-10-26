#O(N) Time Complexity, O(1) Space Complexity
def isValidSubsequence(array, sequence):
    i = 0; j = 0
    while i < len(sequence):
        if sequence[i] == array[j]:
            i += 1
        j += 1

        if j == len(array) and i < len(sequence):
            return False
    return True

print(isValidSubsequence( [1, 1, 1, 1, 1], [1, 1, 1] ))
print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10] ))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 25, 22, 6, -1, 8, 10]))
print(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]))
