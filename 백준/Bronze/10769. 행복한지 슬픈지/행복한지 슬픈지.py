massage=input()

if massage.count(':-)') == 0 and massage.count(':-(') == 0:
    print('none')
elif massage.count(':-)') == massage.count(':-('):
    print('unsure')
elif massage.count(':-)') > massage.count(':-('):
    print('happy')
else:
    print('sad')