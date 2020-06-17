def any_odd(x):
    x ='{0:08b}'.format(abs(x))
# Powers layout
    lenX=(len(x)-1)
    for i in enumerate(x):

        # print(u'\u202B'+f"{2**(i[0])} ", end='')
        if (i[0]==(len(x)-1)):
            print(u'\u202B' + f"{2 ** (i[0])} ", end='')
            print()
        else:
            print(u'\u202B'+f"{2**(i[0])} ", end='')
# iterator spacer
    for i in enumerate(x):
        print(f"{(i[0]+1)} ", end='')
    y=x.replace(""," ")[1:-1]
    print("\n"+y)
    print(f"{x}")
    #
    for i in x[::2]:
        if i=='1':
            z=1
            break
        else:
            z=0
    print(z)
    print()
    # return z
any_odd(31)
# for i in range(1000):
#     print(str(i)+"\n-------")
#     any_odd(i)
