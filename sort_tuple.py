#Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def incr(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=incr)
  
x=[(1, 1), (3, 3), (2, 5),(6,4),(7,6)]
print("Sorted list is: ")
print(sort(x))