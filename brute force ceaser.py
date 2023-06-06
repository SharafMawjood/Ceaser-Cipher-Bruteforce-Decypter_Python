txt = input("Enter the cipher text: ")


for key in range(26):
    cipher = ""
    for t in txt:
        asc = ord(t) - (key + 1)

        if ord(t) >= 97 and ord(t) <= 122:
            asc -= 97
            asc_rem = (asc % 26) + 97

        elif ord(t) >= 65 and ord(t) <= 90:
            asc -= 65
            asc_rem = (asc % 26) + 65

        else:
            asc_rem = ord(t)

        cipher += chr(asc_rem)

    print(f"{key + 1}. {cipher}")