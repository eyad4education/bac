def RacineU(x):
    Un = (1+x) / 2
    valid = False
    while not valid:
        U0 = Un
        Un = (1/2)*(Un+(x/Un))
        valid = abs(((Un-U0) / U0)) < 0.0001
    return Un
print(RacineU(144))
