'''
问题描述：凯撒加密解密算法中的k大小不知道，现在给定一个密文，求解解密后的明文
'''

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


# 结果输出：
# ['ovdthufwvzzpislrlfzhylaolyl', 
# 'nucsgtevuyyohrkqkeygxkznkxk', 
# 'mtbrfsdutxxngqjpjdxfwjymjwj', 
# 'lsaqerctswwmfpioicwevixlivi', 
# 'krzpdqbsrvvleohnhbvduhwkhuh', 
# 'jqyocparquukdngmgauctgvjgtg', 
# 'ipxnbozqpttjcmflfztbsfuifsf', 
# 'howmanypossiblekeysarethere',  ##### 这句是对的
# 'gnvlzmxonrrhakdjdxrzqdsgdqd', 
# 'fmukylwnmqqgzjcicwqypcrfcpc', 
# 'eltjxkvmlppfyibhbvpxobqebob', 
# 'dksiwjulkooexhagauownapdana', 
# 'cjrhvitkjnndwgzfztnvmzoczmz',
# 'biqguhsjimmcvfyeysmulynbyly', 
# 'ahpftgrihllbuexdxrltkxmaxkx', 
# 'zgoesfqhgkkatdwcwqksjwlzwjw', 
# 'yfndrepgfjjzscvbvpjrivkyviv', 
# 'xemcqdofeiiyrbuauoiqhujxuhu', 
# 'wdlbpcnedhhxqatztnhpgtiwtgt', 
# 'vckaobmdcggwpzsysmgofshvsfs', 
# 'ubjznalcbffvoyrxrlfnergurer', 
# 'taiymzkbaeeunxqwqkemdqftqdq', 
# 'szhxlyjazddtmwpvpjdlcpespcp', 
# 'rygwkxizyccslvouoickbodrobo', 
# 'qxfvjwhyxbbrkuntnhbjancqnan', 
# 'pweuivgxwaaqjtmsmgaizmbpmzm']

if __name__ == '__main__':
    main()
