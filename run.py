import platform,os
bit = platform.architecture()[0]
print(' CHECKING FOR UPDATES');os.system('git pull')
try:
    if bit == '32bit':
        from data import NEPAL32
    elif bit == '64bit':
        from data import NEPAL64
    else: exit(" SORRY YOUR DEVICE DOESN'T SUPPORT THIS TOOL USE 32/64 BIT PHONE");exit()
except: 
    if bit == '32bit':
        import NEPAL32
    elif bit == '64bit':
        import NEPAL64
    else: exit(" SORRY YOUR DEVICE DOESN'T SUPPORT THIS TOOL USE 32/64 BIT PHONE");exit()
        
