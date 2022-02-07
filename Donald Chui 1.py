print('DONALD CHUI')
print('TONBRIDGE SCHOOL')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encrypted = input()
encrypt = list(encrypted)
decrypt = ''
decrypt += encrypt[0]
for i in range(1, len(encrypted)):
    current = alphabet.index(encrypt[i])
    last = alphabet.index(encrypt[i-1])
    original = current-last-1
    if original < 0:
        original += 26
    decrypt += alphabet[original]
decrypted = str(decrypt)
print(decrypted)