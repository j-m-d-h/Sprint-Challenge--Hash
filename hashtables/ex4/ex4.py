def has_negatives(a):
    cache = {}
    result = []
    for num in a:
        if num == 0:
            pass
        else:
            cache[num] = False
        if -num in cache:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
