a = 0
b = 1
try:
    c = b / a
except Exception as inst:
    print('Except: {}'.format(inst))
else:
    print('Else')

print('Call')
