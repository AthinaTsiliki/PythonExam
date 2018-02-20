numsList = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def intGoToLatin(num):

    latinNum = ''

    while num > 0:
        for i, r in numsList:
            while num >= i:
                latinNum += r
                num -= i
        return latinNum
user_input = int(raw_input("Give me an integer and I will convert it to a latin number: "))
print intGoToLatin(user_input)
