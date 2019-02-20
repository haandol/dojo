import re


def reverse(s):
    return s[::-1]

def fix_tag(s):
    pat = r'>(\w+)\/<(\w+)>(\w+)<'
    return re.sub(pat, r'<\g<3>>\g<2></\g<1>>', s)


s = 'Amazon TV <em>Alexa</em> And <b>Echo</b>'
print(fix_tag(reverse(s)))