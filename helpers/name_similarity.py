def name_similarity(str1: str, str2: str):
    prev = list(range(len(str2) + 1))
    for ind1, ch1 in enumerate(str1, 1):
        curr = [ind1]
        for ind2, ch2 in enumerate(str2, 1):
            curr.append(min(
                prev[ind2] + 1,
                curr[ind2-1] + 1,
                prev[ind2-1] + (ch1 != ch2)
            ))
        prev = curr
    return round(prev[-1]/10, 2)

