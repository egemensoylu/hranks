def bitwiseAnd(N, K):
    # Write your code here
    max_possible = 0
    for a in range(K - 10, N + 1):
        for b in range(a + 1, N + 1):
            if b <= N:
                bwa = a & b
                # print(a, b, bwa)
                if bwa > max_possible:
                    if bwa >= K:
                        break
                    else:
                        max_possible = bwa
    return max_possible


if __name__ == '__main__':

    checkFile = open('check.txt', 'r')

    with open('input.txt', 'r') as f:
        for line in f:
            line_data = line.split(' ')
            n = int(line_data[0])
            k = int(line_data[1])
            res = bitwiseAnd(n, k)

            check = checkFile.readline().split('\n')[0]
            if int(res) != int(check):
                print(n, k, res, check)
# fptr.write(str(res) + '\n')
# fptr.close()

