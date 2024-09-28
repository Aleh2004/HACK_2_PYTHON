"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if not s:
        return [0]

    # Verificar si todos los elementos son enteros
    if all(isinstance(x, int) for x in s):
        # Si la lista contiene solo enteros, devolvemos la lista de enteros tal cual
        return s
    
    # Lista contiene otros tipos de datos
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(str(i + 1))
        else:
            result.append(i + 1)
    
    return result