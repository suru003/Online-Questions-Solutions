# Q1
li = [1,2,3,4,5,True,"Abc",[2,3,["hello"]]]
# 1. add a element
li.append("new_element")
print(li)

# 2. add a element at specific index
li.insert(2,"inserted at 2")
print(li)

# 3. extend with other lists
li2 = (1,34,3,4,{12,23},{1:"one",2:"two"})
li.extend(li2)
print(li)

# 4. count the frequency of elements in the list
# Fun Fact: count treats True as 1 and False as 0 and vice-versa
print(li.count(True))

# 5. reverse the list
li.reverse()
print(li)


#-------------------------------------------------------------------------------------------------------

# Q2
keys = {'a', 'e', 'i', 'o', 'u' }

# 1. Initialize dictionary with keyset
dic = dict.fromkeys(keys)
print(dic)

# 2. Initialize dictionary with keyset with a default value
dic = dict.fromkeys(keys,"Default")
print(dic)

# 3. Search for a key if a key doesn't exists return False otherwise it's value
dic.get('a','Not Found')
dic.get('s','Not Found')
print(dic)

# 4. pop out the last key:value in dictionary
dic['s']='Hello'
print("popped ",dic.popitem())

# 5. Update the dictionary using another dictionary
dic2 = {'a':'vowel','b':'consonent'}
dic.update(dic2)
print(dic)
