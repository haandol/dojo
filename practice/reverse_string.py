import re


def reverse(s):
    n = len(s)
    on_tag = True
    tag = []
    res = []
    for i in range(n-1, -1, -1):
        if s[i] == '>':
            tag.append(s[i])
            on_tag = True
        elif s[i] == '<':
            tag.append(s[i])
            on_tag = False
            res.extend(tag[::-1])
            tag = []
        elif on_tag:
            tag.append(s[i])
        else:
            res.append(s[i])
    return ''.join(res)


def fix_tag(s):
    pat = r'(<b>)(\w+)(</b>)'
    return re.sub(pat, r'\g<3>\g<2>\g<1>', s)


s = 'Amazon TV <b>Alexa</b>'
print(reverse(fix_tag(s)))