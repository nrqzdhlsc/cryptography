cipher = 'JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX'

frequency_dic = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.043,
    'e': 0.127,
    'f': 0.022,
    'g': 0.020,
    'h': 0.061,
    'i': 0.070,
    'j': 0.002,
    'k': 0.008,
    'l': 0.040,
    'm': 0.024,
    'n': 0.067,
    'o': 0.015,
    'p': 0.019,
    'q': 0.001,
    'r': 0.060,
    's': 0.063,
    't': 0.091,
    'u': 0.028,
    'v': 0.010,
    'w': 0.024,
    'x': 0.002,
    'y': 0.020,
    'z': 0.001
}

# print(frequency_dic['z'])

# 统计文本中词频
real_freq = {}
for item in cipher:
    if real_freq.get(item) == None:
        real_freq[item] = round(1 / len(cipher), 3)
    else:
        real_freq[item] += 1 / len(cipher)
        real_freq[item] = round(real_freq[item], 3)

# print(real_freq)

# 结果

'''
{
    'J': 0.036, 
    'G': 0.076, 
    'R': 0.028, 
    'M': 0.016, 
    'Q': 0.104, 
    'O': 0.064, 
    'Y': 0.012, 
    'H': 0.056, 
    'V': 0.06, 
    'B': 0.048, 
    'W': 0.084, 
    'F': 0.148, 
    'P': 0.04, 
    'D': 0.008, 
    'Z': 0.028, 
    'K': 0.012, 
    'E': 0.016, 
    'I': 0.036, 
    'C': 0.012, 
    'L': 0.068, 
    'A': 0.012, 
    'S': 0.008, 
    'X': 0.004}
'''

source = []
target = []
for key, value in frequency_dic.items():
    source.append((key, value))

for key, value in real_freq.items():
    target.append((key, value))

# 根据value排序
source = sorted(source, key=lambda x: -x[1])
target = sorted(target, key=lambda x: -x[1])

print("source: ", source)
print("\n")
print("target: ", target)
print("\n")

print(len(source))
print(len(target))

cipher2plain = {}
for i in range(len(target)):
    cipher2plain[target[i][0]] = source[i][0]

print("cipher2plain: ", cipher2plain)

plain = ""
for item in cipher:
    plain += cipher2plain[item]

print("plain: ", plain)

# cimftsyirfhdcamatelarieevtielewmpdggdcuwttsbudwpneoeitheweaagsiasleierasnlrnmnsnevfeitadnadatsnpeadyndnynekencimftdsnacheleathrtaeeltstheltsbelsieaecuiethrnrnmstheiachelesneriththeungsitunrtetiuthhskeoeidathrtauchachelearieuaurwwmtidodrwtsbierj
# 算法解的不对哎，需要再改进
# Modified Time: 20191022





