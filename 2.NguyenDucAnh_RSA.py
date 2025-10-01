#  p=17, q=23, e=5


def rsa_encrypt(Plaintext, p, q, e):
    n = p * q
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
    cipher = rsa_encrypt(Plaintext, p, q, e)
    print("Sau mã hóa:", cipher)


