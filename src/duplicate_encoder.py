def duplicate_encode(word):
    word = word.lower()
    frecuencias = {}
    
    for char in word:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
            
    resultado = []
    for char in word:
        if frecuencias[char] == 1:
            resultado.append("(")
        else:
            resultado.append(")")
            
    return "".join(resultado)

    assert_equals(duplicate_encode("din"),"(((")
    assert_equals(duplicate_encode("recede"),"()()()")
    assert_equals(duplicate_encode("Success"),")())())","should ignore case")
    assert_equals(duplicate_encode("(( @"),"))((")