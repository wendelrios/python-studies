conjunto = {1,2,3,4,5}
conjunto.add(4)
print(conjunto)
conjunto.discard(2)
print(conjunto)

s1 = {'fluminense','flamengo','vasco','botafogo'}

s2 = {'corinthians','sao paulo','santos','palmeiras'}

s3 = s1.union(s2)
print(s3)

s4 = s3.intersection(s1)
print(s4)