#  p=17, q=23, e=5




def timnghichdao(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def mahoa(Plaintext, n, e):
    cipher = []
    for char in Plaintext:
        m = ord(char)
        c = pow(m, e, n)
        cipher.append(c)
    return cipher

if __name__ == "__main__":
    p = 17
    q = 23
    e = 5
    Plaintext = "NguyenDucAnh"
    n = p * q
    z = (p - 1) * (q - 1)
    d = timnghichdao(e, z)
    print("n =", n)
    print("z =", z)
    print("Khóa công khai (n, e):", (n, e))
    print("Khóa bí mật (n, d):", (n, d))
    cipher = mahoa(Plaintext, n, e)
    print("Sau mã hóa:", cipher)
    
