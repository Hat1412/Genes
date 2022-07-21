import json

def translate(s):
    a = 0
    b = a + 3
    s_new = ""

    for _ in range(len(s) // 3):
        s_new += f"{data[s[a:b]]} "

        a = b
        b = a + 3

    return s_new

def comp(s):
    strand = {"A":"U","T":"A","C":"G","G":"C","U":"T"}
    comp_s = ""

    for i in s:
        comp_s += strand[i]

    return comp_s

s = "AUGUAUUUCGCGCGCGGGGGAUG"

with open("codones.json") as f:
    data = json.load(f)

s_ = comp(s)

print("Original Strand:",s)
print("Complementary Strand:",s_)
print("Translated Strand:",translate(s))