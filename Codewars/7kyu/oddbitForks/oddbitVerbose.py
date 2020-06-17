def any_odd(x):
    x ='{0:04b}'.format(x)
    count=''
    for i in enumerate(x):
        print(u'\u202B'+f"{2**(i[0])} ", end='')
    print()
    for i in enumerate(x):
        print(f"{(i[0]+1)} ", end='')
    y=x.replace(""," ")[1:-1]
    print("\n"+y)
    print(f"{x}")
    for i in x[::2]:
        if i=='1':
            z=1
            break
        else:
            z=0
    print(z)
    print()
    # return z
any_odd(67)
for i in range(1000):
    print(str(i)+"\n-------")
    any_odd(i)
