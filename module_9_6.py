def all_variants(text):
    for i in range(1, len(text)+1):
        for j in range(len(text)+1-i):
            yield text[j:i+j]

a = all_variants("abc")
for i in a:
    print(i)
