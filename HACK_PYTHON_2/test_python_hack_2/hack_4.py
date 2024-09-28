"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    if len(s) > 3:
        result = s[1:-1]
    else:
        # Devolver la cadena original si la longitud es 2 o menor
        result = s
    
    return result
