no_publicize, publicize, cost = input().split()
publicize = int(publicize)
no_publicize = int(no_publicize)
cost = int(cost)

if (publicize - cost) > no_publicize:
    print('advertise')
elif (publicize - cost) < no_publicize:
    print('do not advertise')
else:
    print('does not matter')
