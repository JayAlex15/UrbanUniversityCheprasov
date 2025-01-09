def all_variants(text):
    lenght_text = len(text)
    a = 0
    b = 0
    for i in range(1, lenght_text+1):
        count = 0
        for a in range(0, lenght_text):
            count += 1
            b = a + i
            if count > 1 + lenght_text - i:
                continue
            yield text[a:b]

a = all_variants("abc")
for i in a:
    print(i)