def tower_builder(n_floors, block_size):
    w, h = block_size
    z=''
    for i in range(n_floors):
        for j in range(h):
            for k in range(0, n_floors-i):
                z += ' '*w
            for k in range(0, 2*i+1):
                z += '*'*w
            z += '\n'
        # z += '\n'
    print(z)

tower_builder(6,(2,1))

# def pyramid(n):
#     z=''
#     for i in range(n)::
#         for k in range(0, n-i):
#             z += '   '
#         for k in range(0, 2*i+1):
#             z += ' * '
#         z += '\n'
#         # z += '\n'
#     print(z)

# pyramid(6)