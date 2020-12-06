
#codigo que pede ao usuario um numero N e exibe os numeros primos entre 1 e N
valor = int(input('digite um numero: '));

for i in range(1, valor+1):
  divisores = 0;
  for j in range(1, valor+1):
    resto = i%j;
    if resto == 0:
      divisores+=1;
  if divisores==2:
    print(i)

#codigo que cria uma matriz 3x3 preenchidas por x;
for i in range(3):
  for j in range(3):
    print('x', end='');
  print();


#codigo para usar while
numero = 0
soma = 0;
media = 0;

while numero < 4:
  nota = float(input('digite sua nota: '));
  soma+=nota;
  numero+=1;

media = soma/4;
print('media: {}'.format(media));
  
