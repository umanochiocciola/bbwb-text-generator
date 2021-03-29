
STRING = input('string: ')

OUT = ''
for i in STRING:
    boye = ord(i)

    check = [10, 9, 8, 7, 6, 5, 4]

    bob = 1
    for C in check:
        if boye % C == 0:
            cont = '#' + '+'*int(boye/C) + '^#[>v' + '+'*C + '^#<v-^#]>v:'
            bob = 0
            break
        
        if (boye-1) % C == 0:
            cont = '#' + '+'*int((boye-1)/C) + '^#[>v' + '+'*C + '^#<v-^#]>v+:'
            bob = 0
            break

    if bob:
        cont = '#' + '+'*boye + ':'

    OUT += cont

print(OUT)

