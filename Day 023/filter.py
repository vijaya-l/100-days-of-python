# 1filter the 'r' names

names = ["adya", "anu", "reema", "riya"]
r_names = filter(lambda n: n[0] == "r", names)
print(list(r_names))

print([f" your name is {name}" for name in names if len(name)<5])

#2. filter the even numbers
nums=[1,2,4,5,6,7,8]
num= filter(lambda n: n%2==0 , nums)
print(list(num))

# 3.define function and remove all -ve numbers

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))

nums=[2,4,-5,7,-8,-1]
print(remove_negatives(nums))