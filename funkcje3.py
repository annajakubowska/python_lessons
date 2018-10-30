def funkcja(*args,glue=':'):
    result = ""
    for elem in args:
        if len(elem) > 3:
            result =result + elem + glue
    return result
    
print (funkcja ("anna","jakubowska","i","nokia"))

print (funkcja ("anna","jakubowska","i","nokia",glue='-'))