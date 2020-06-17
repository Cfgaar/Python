def any_odd(x):
    x ='{0:032b}'.format(abs(x))
    for i in x[::2]:
        if i=='1':
            z=1
            break
        else:
            z=0
    return z
