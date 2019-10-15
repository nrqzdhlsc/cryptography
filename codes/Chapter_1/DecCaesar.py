cipher = "OVDTHUFWVZZPISLRLFZHYLAOLYL"
MOD = 26

def dec(c, k):
    # c: 大写字母
    # k: 字母移动位数
    # 密文到明文，即大写到小写
    if ord(c) not in range(ord('A'), ord('Z') + 1):
        return 0
    od = ord('a') + (ord(c) - ord('A') - k) % MOD
    return chr(od)

def main():
    res = []
    for k in range(26):
        temp = ''
        for item in cipher:
            temp += dec(item, k)
        res.append(temp)

    print(res)

if __name__ == '__main__':
    main()