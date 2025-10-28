#Implement the function that meets the specifications below.
def keys_with_value(aDict, target):
 """
 aDict: a dictionary
 target: an integer or string
 Assume that keys and values in aDict are integers or strings.
 Returns a sorted list of the keys in aDict with the value target.
 If aDict does not contain the value target, returns an empty list.
 """
 # Your code here
 target_keys = []
 for i in aDict.keys():
     if aDict[i] == target:
         target_keys.append(i)
 return sorted(target_keys)

#Implement the function that meets the specifications below.
def all_positive(d):
 """
 d is a dictionary that maps int:list
 Suppose an element in d is a key k mapping to value v (a non-empty list).
 Returns the sorted list of all k whose v elements sums up to a
 positive value.
 """
 # Your code here
 L = []
 for k,v in d.items():
     if sum(v) > 0:
         L.append(k)
 return sorted(L)