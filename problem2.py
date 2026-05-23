def palindrome(n):
    b = list(map(str,n))

    for i in b:
        if i == " ":
            b.remove(" ")

    string = "".join(b)
    half = len(string)/2
    rounded = int(half)
    if string[:rounded] == string[len(string):rounded:-1]:
        return True
    else:
        return False

inp = input()
n = inp.lower()
print(palindrome(n))




