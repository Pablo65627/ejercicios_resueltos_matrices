
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    
    return sorted([x ** 2 for x in array1]) == sorted(array2)


if __name__ == '__main__':
    a1 = [121]
    a2 = [121*121]
    '''
    assert comp(a1, a2)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) '''
    #a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    #a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    #assert_equals(comp(a1, a2), False)
    #a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    #a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    #assert_equals(comp(a1, a2), False)