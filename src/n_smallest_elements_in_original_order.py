def first_n_smallest(arr, n):
    indexed_arr = list(enumerate(arr))
    
    sorted_by_val = sorted(indexed_arr, key=lambda x: x[1])
    
    smallest_n = sorted_by_val[:n]
    
    smallest_n.sort(key=lambda x: x[0])
    
    return [x[1] for x in smallest_n]

if __name__ == '__main__':
  
    assert first_n_smallest([1,2,3,4,5],3) == [1,2,3]
    assert first_n_smallest([5,4,3,2,1],3 )== [3,2,1] 
    assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
    assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
    assert first_n_smallest([1,2,3,4,5],0) == []
    assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
    assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
    assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
    assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
    assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]