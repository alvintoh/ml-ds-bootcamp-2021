# Scope - what variables do I have access to?
total = 10


def count(total):
    total += 1
    return total


print(count(count(count(total))))

# 1 - Start with local
# 2 - Parent local?
# 3 - Global
# 4 - Built in python functions.