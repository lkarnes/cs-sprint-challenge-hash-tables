def intersection(arrays):
    results = []
    cache = {}
    for i in arrays:
        for j in i:
            if j not in cache:
                cache[j] = 1
            else: 
                cache[j] = cache[j] + 1
            if cache[j] >= len(arrays):
                results.append(j)
    return results

print(intersection([[1,2,3],
            [1,4,5],
            [1,6,7]]))
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    print(intersection(arrays))
