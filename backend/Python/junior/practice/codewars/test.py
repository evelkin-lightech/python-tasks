def snail(snail_map):
    result = []
    if snail_map and snail_map[0]:
        size = len(snail_map)
        for n in range((size + 1) // 2):
            for i in range(n, size - n):
                result.append(snail_map[n][i])
            for j in range(n + 1, size - n):
                result.append(snail_map[j][- 1 - n])
            for i in range(n + 2, size - n + 1):
                result.append(snail_map[-1 - n][-i])
            for j in range(n + 2, size - n):
                result.append(snail_map[-j][n])
    return result


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(snail(array))
