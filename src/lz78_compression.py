import re

def encoder(data):
    dictionary = {'': 0}
    dict_size = 1
    output = []
    
    current_str = ""
    i = 0
    n = len(data)
    
    while i < n:
        current_str += data[i]
        
        if current_str not in dictionary:
            prefix = current_str[:-1]
            last_char = current_str[-1]
            
            output.append(f"{dictionary[prefix]}{last_char}")
            
            dictionary[current_str] = dict_size
            dict_size += 1
            
            current_str = ""
        
        i += 1
        
    if current_str:
        output.append(str(dictionary[current_str]))
        
    return "".join(output)

def decoder(data):
    dictionary = {0: ''}
    dict_size = 1
    output = []
    
    tokens = re.findall(r'(\d+)([A-Z]?)', data)
    
    for index_str, char in tokens:
        index = int(index_str)
        string_val = dictionary[index] + char
        output.append(string_val)
        
        dictionary[dict_size] = string_val
        dict_size += 1
        
    return "".join(output)


if __name__ == "__main__":
    def test_encoder():
        assert encoder("ABAABABAABAB") == "0A0B1A2A4A4B"
        assert encoder('ABAABABAABABAA') == '0A0B1A2A4A4B3', 'ABAABABAABABAA'
        assert encoder('ABBCBCABABCAABCAABBCAA') == '0A0B2C3A2A4A6B6', 'ABBCBCABABCAABCAABBCAA'
        assert encoder('AAAAAAAAAAAAAAA') == '0A1A2A3A4A', 'AAAAAAAAAAAAAAA'
        assert encoder('ABCABCABCABCABCABC') == '0A0B0C1B3A2C4C7A6', 'ABCABCABCABCABCABC'
        assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C', 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC'
        print("TEST ENCODER: SUPERADO ✅")
        
    def test_decoder():
        assert decoder('0A0B1A2A4A4B') == 'ABAABABAABAB', '0A0B1A2A4A4B'
        assert decoder('0A0B1A2A4A4B3') == 'ABAABABAABABAA', '0A0B1A2A4A4B3'
        assert decoder('0A0B2C3A2A4A6B6') == 'ABBCBCABABCAABCAABBCAA', '0A0B2C3A2A4A6B6'
        assert decoder('0A1A2A3A4A') == 'AAAAAAAAAAAAAAA', '0A1A2A3A4A'
        assert decoder('0A0B0C1B3A2C4C7A6') == 'ABCABCABCABCABCABC', '0A0B0C1B3A2C4C7A6'
        assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C') == 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'
        print("TEST DECODER: SUPERADO ✅")

    test_encoder()
    test_decoder()