import platform

bit = platform.architecture()[0]
if bit == '64bit':
    import attack64
else bit == '32bit':
    import attack32
