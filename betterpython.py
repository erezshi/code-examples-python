#ternary condition
condition = True
x = 1 if condition else 0

#Large numbers
ternary condition
n1 = 10_000_000_000
n2 = 100_000_000
total = n1+n2
print(f'{total:,}')
10,100,000,000

#enumerate - display the position of the value in the list
names = ['David', 'Fisher', 'Davidson', 'Yoda']
or index, name in enumerate(names, start=1):
  print(index, name)

1 David
2 Fisher
3 Davidson
4 Yoda

# unpacking multiple lists
python unpack multiple lists together 
titles = ['Mr', 'Ms', 'Mrs', 'Mr']
names = ['David', 'Diana', 'Mor', 'Joe']
for name, title in zip(names, titles):
   print(f'Hey {title} {name} nice to meet you')

Hey Mr David nice to meet you
Hey Ms Diana nice to meet you
Hey Mrs Mor nice to meet you
Hey Mr Joe nice to meet you
