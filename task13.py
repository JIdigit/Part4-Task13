def superDigit(n, k):
    super_num = n*k
    # print(len(super_num))
    if len(super_num) == 1:
        return super_num
    else:
        temp_num = 0
        for i in super_num:
            temp_num = temp_num + int(i)
        return superDigit(str(temp_num),1)
        
        
    return 'hey'

if __name__ == '__main__':

    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = print(superDigit(n, k))
