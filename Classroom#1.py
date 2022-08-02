l = ['Jack', 'Mike', 'John']

def lower(t):
    return t.lower()

def upper(t):
    return t.upper()

print(list(map(lower, l)))
print(list(map(upper, l)))