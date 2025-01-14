import re

# Test z kwantyfikatorem "+"
print("Dopasowanie z '+':", re.findall('a+', 'aaaa'))

# Test z kwantyfikatorem "+?" (leniwy)
print("Dopasowanie z '+?':", re.findall('a+?', 'aaaa'))

# Test z kwantyfikatorem "*"
print("Dopasowanie z '*':", re.findall('a*', 'aaaa'))

# Test z kwantyfikatorem "*?" (leniwy)
print("Dopasowanie z '*?':", re.findall('a*?', 'aaaa'))

# Test z kwantyfikatorem "?"
print("Dopasowanie z '?':", re.findall('a?', 'aaaa'))

# Test z kwantyfikatorem "??" (leniwy)
print("Dopasowanie z '??':", re.findall('a??', 'aaaa'))
