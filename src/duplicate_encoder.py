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

if __name__ == "__main__":
    print(duplicate_encode("din"))
    print(duplicate_encode("recede"))
    print(duplicate_encode("Success"))
    print(duplicate_encode("(( @"))