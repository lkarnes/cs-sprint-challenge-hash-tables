def has_negatives(a):
    result = []
    matches = {}
    for i in a:
        if i < 0:
            if -i not in matches:
                matches[-i] = False
            else:
                result.append(-i)
        else:
            if i not in matches:
                matches[i] = False
            else: 
                result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
