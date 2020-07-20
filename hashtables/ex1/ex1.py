def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    if length == 2:
        if weights[0]+weights[1] == limit:
            return [1,0]
    for i in weights:
        if i not in cache:
            cache[i] = limit - i
        if limit-i in weights:
            return [weights.index(cache[i]), weights.index(i)]