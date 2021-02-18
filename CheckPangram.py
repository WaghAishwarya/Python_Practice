
def ispangram(str):
    x = "abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i not in str.lower():
            return False

    return True


s = 'the quick brown fox jumps over the lazy dog'
y = 'the quick brown fox jumps over the dog'

print(ispangram(s))
print(ispangram(y))