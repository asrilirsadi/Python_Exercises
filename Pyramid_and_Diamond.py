n = int(input('Input n: '))

def pyramid(n):
    z=''
    for i in range(n):
        for j in range(0, n-i):
            z += '   '
        for j in range(0, 2*i+1):
            z += ' * '
        z += '\n'
    print(z)
pyramid(n)

def reversed_pyramid(n):
    z = ''
    for i in range(n):
        for j in range(1, i+2):
            z += '   '
        for j in range(2*(n-i)-1):
            z += ' * '
        z += '\n'
    print(z)
reversed_pyramid(n)

def diamond(n):
    z=''
    for i in range(n-1):
        for j in range(0, n-i):
            z += '   '
        for j in range(0, 2*i+1):
            z += ' * '
        z += '\n'
    for i in range(n):
        for j in range(1, i+2):
            z += '   '
        for j in range(2*(n-i)-1):
            z += ' * '
        z += '\n'
    print(z)
diamond(n)

def hollow_pyramid(n):
    z=''
    for i in range(n):
        for j in range(n-i):
            z += '   '
        
        if i == 0:
            z += ' * '
        elif i > 0 and i < n-1: 
            z += ' * '
            for k in range(2*(i-1)+1):
                z += '   ' 
            z += ' * '
        elif i < n:
            for l in range(2*(n-1)+1):
                z += ' * '

        z += '\n'
    print(z)
hollow_pyramid(n)

def hollow_reversed_pyramid(n):
    z=''
    for i in range(n):
        for j in range(i+1):
            z += '   '
        if i==0:
            for j in range(2*(n-i)-1):
                z += ' * '
        elif i>0 and i<n-1:
            z += ' * '
            for j in range(1, 2*(n-i)-2):
                z += '   '
            z += ' * '
        elif i < n:
            z += ' * '
        # for j in range(0, 2*(n-i)-1):
        #     z += ' * '
        z += '\n'
    print(z)
hollow_reversed_pyramid(n)

def hollow_diamond(n):
    z=''
    for i in range(n-1):
        for j in range(n-i):
            z += '   '
        if i == 0:
            z += ' * '
        elif i > 0 and i < n-1: 
            z += ' * '
            for k in range(2*(i-1)+1):
                z += '   ' 
            z += ' * '
        z += '\n'
    for i in range(n):
        for j in range(1, i+2):
            z += '   '
        if i>=0 and i<n-1:
            z += ' * '
            for j in range(0, 2*(n-i)-3):
                z += '   '
            z += ' * '
        elif i < n:
            z += ' * '
    
        z += '\n'
    print(z)
hollow_diamond(n)
