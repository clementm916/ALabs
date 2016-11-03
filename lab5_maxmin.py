def find_max_min(l):
    """Returns the smallest and largest items in a list"""
    l_min = min(l) #get smallest item
    l_max =max(l) #get largest item

    if l_min == l_max: #if smallest and largest items are equal 
    	return [l_min] #return the smalest

    


    return [l_min,l_max] #else return a list of the smallest followed by the largest

print find_max_min([2,2,2,2,2])
