#short approach
def findDuplicate(arr: list, n: int):
    diff = n - len(set(arr))
    summ = sum(arr) - sum(set(arr))
    return summ // diff


#long approach
def findDuplicate(arr: list, n: int):
    #Phase1
    tortoise = hare = arr[0]  #starting from 0th index
    while True:  #Running loop till tortoise and hare meet
        tortoise = arr[tortoise]  #tortoise moves 2x faster than hare
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    #phase2
    # Find the "entrance" to the cycle.
    tortoise = arr[
        0]  #now hare is lost in cycle and tortoise will find it from start
    while tortoise != hare:  #wherever tortoise meets hare cycle is detected
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare
