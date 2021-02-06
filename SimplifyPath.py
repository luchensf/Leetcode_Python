def simplifyPath(path):
    s = []
    for i in path.split('/'):
        if i == '..':
            if s: s.pop()
        elif i not in ['.', '']:
            s.append(i)
    return '/' + '/'.join(s)


