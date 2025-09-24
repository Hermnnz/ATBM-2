
    
# Với mã hóa Caesar là trường hợp đặc biệt của mã hóa thay thế với k=3, còn mã hóa thay thế thì k có thể là bất kỳ số nào từ 1 đến 25.


Bangchucai = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
        6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
        12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
        18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
        24: 'Y', 25: 'Z'
    }
def mahoa_thaythe(P, k):
    mahoa = ""
    for i in P:
        if i == ' ':
            mahoa += ' '
        else:
            for key, value in Bangchucai.items():
                if i == value:
                    x = (key + k) % 26
                    mahoa += Bangchucai[x]
                    break
    return mahoa

P = "NGUYEN DUC ANH"
k=2
print(mahoa_thaythe(P, k))