nome = input('Digite seu nome: ');
idade = int(input('Digite sua idade: '));
nota1 = float(input('Digite sua primeira nota: '));
nota2 = float(input('Digite sua segunda nota: '));
media = (nota1+nota2)/2;

print(nome + ' tem {}' .format(idade) + ' anos');

if media>=5 and media<7:
  print('aluno esta de recuperacao')
elif media<5:
  print('aluno esta reprovado')
else:
  print('aluno foi aprovado');
