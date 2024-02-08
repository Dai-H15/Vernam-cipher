print("バーナム暗号に基づいて暗号化を行い、2進数の羅列を返すプログラム")


def encript(user):
    result = []
    print("\n各数値は何ビットの2進数で表現しますか？")
    bit_len = int(input(">>> "))
    print("\naの開始位置は？(0 or 97)")
    st_a = 97 - int(input(">>> "))

    for u in user:
        print(f"\n' {u} ' に対する暗号キーを入力: ")
        key = input(">>>")
        i_u = ord(u) - st_a
        i_key = int(key, 2)
        print(f"\n---\n '{u}' = {i_u} ({bin(i_u)[2::]})  key = {i_key} ({bin(i_key)[2::]})\n---\n")
        xor = i_u ^ i_key
        print(bin(xor))
        if len(bin(xor))-2 < bit_len:
            s_xor = "0" * (bit_len-(len(bin(xor))-2)) + bin(xor)[2::]
            print(f"{bit_len}ビットに補完")
            print(s_xor)
        else:
            s_xor = bin(xor)[2::]
        result.append(s_xor)
    print(f"\n暗号化 結果: { ' '.join(result)}")
    return result


def decript(enc_texts):
    print("\naの開始位置は？(0 or 97)")
    st_a = 97 - int(input(">>> "))

    print(enc_texts)
    result = ""
    n = 1
    for text in enc_texts:
        i_text = int(text, 2)
        i_key = int(input(f"\n{text} に対するKeyを入力 ({n}文字目)\n>>> "), 2)
        xor = i_text ^ i_key
        s_xor = chr(xor + st_a)
        result += s_xor
        n += 1
    print(f"\n復号化 結果: {result}")
    return result


if input("1. 暗号化\n2. 復号化\n>>>") == "1":
    user = input("\n暗号化する文字列を入力 >>> ")
    result = encript(user)
    if input("復号化しますか？ y/n \n>>>") == "y":
        decript(result)
else:
    enc_texts = input("復号化する2進数の羅列を空白区切りで入力\n>>>").split(" ")
    print(f"対象 : {enc_texts}")
    result = decript(enc_texts)
    if input("暗号化しますか？ y/n \n>>>") == "y":
        result = encript(result)
