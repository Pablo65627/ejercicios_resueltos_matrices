import re
from tkinter.filedialog import test

def encoder(data):
    dictionary = {'': 0}
    dict_size = 1
    output = []
    
    current_str = ""
    
    for char in data:
        current_str += char
        
        if current_str not in dictionary:
            prefix = current_str[:-1]
            last_char = current_str[-1]

            output.append(f"{dictionary[prefix]}{last_char}")
            
            dictionary[current_str] = dict_size
            dict_size += 1
            
            current_str = ""
        
    if current_str:
        output.append(str(dictionary[current_str]))
        
    return "".join(output)

def decoder(data):
    dictionary = {0: ''}
    dict_size = 1
    output = []

    tokens = re.findall(r'(\d+)([A-Z])|(\d+)$', data)
    
    for match in tokens:
        if match[2]:
            index = int(match[2])
            char = ""
        else:
            index = int(match[0])
            char = match[1]
            
        string_val = dictionary[index] + char
        output.append(string_val)
        
        dictionary[dict_size] = string_val
        dict_size += 1
        
    return "".join(output)


if __name__ == "__main__":


    def test_encoder():
        assert_equals(encoder('ABAABABAABAB'), '0A0B1A2A4A4B', 'ABAABABAABAB')
        assert_equals(encoder('ABAABABAABABAA'), '0A0B1A2A4A4B3', 'ABAABABAABABAA')
        assert_equals(encoder('ABBCBCABABCAABCAABBCAA'), '0A0B2C3A2A4A6B6', 'ABBCBCABABCAABCAABBCAA')
        assert_equals(encoder('AAAAAAAAAAAAAAA'), '0A1A2A3A4A', 'AAAAAAAAAAAAAAA')
        assert_equals(encoder('ABCABCABCABCABCABC'), '0A0B0C1B3A2C4C7A6', 'ABCABCABCABCABCABC')
        assert_equals(encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC'), '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C', 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC')
        
    def test_encoder():
        assert_equals(decoder('0A0B1A2A4A4B'), 'ABAABABAABAB', '0A0B1A2A4A4B')
        assert_equals(decoder('0A0B1A2A4A4B3'), 'ABAABABAABABAA', '0A0B1A2A4A4B3')
        assert_equals(decoder('0A0B2C3A2A4A6B6'), 'ABBCBCABABCAABCAABBCAA', '0A0B2C3A2A4A6B6')
        assert_equals(decoder('0A1A2A3A4A'), 'AAAAAAAAAAAAAAA', '0A1A2A3A4A')
        assert_equals(decoder('0A0B0C1B3A2C4C7A6'), 'ABCABCABCABCABCABC', '0A0B0C1B3A2C4C7A6')
        assert_equals(decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'), 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')