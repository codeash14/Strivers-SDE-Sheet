def missingAndRepeating(arr, n):
    missing = (n * (n + 1) // 2) - sum(set(arr))
    repeating = sum(arr) - sum(set(arr))
    return missing, repeating
