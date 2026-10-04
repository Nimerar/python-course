# sp=['Anya','Sasha','Misha','Kostya','Gelya']
# count=0
# for i in sp:
#     count+=1
#     print (count,i)
# print(sp[:1])
# print(sp[1:])
#
# nums=[1,2,3,5,7,11,13]
# print(nums)
# nums.append(17)
# print(nums)
# if 3 in nums:
#     print('Yeaaa')
# else:
#     print('Nopeee')
nums=[-5,-2,-9]
total=0
for num in nums:
    total+=num
print (total)
biggest=nums[0]
for i in range (len(nums)):
    if nums[i]>biggest:
        biggest=nums[i]
print (biggest)


smallest=nums[0]
for i in  range (len(nums)):
    if smallest>nums[i]:
        smallest=nums[i]
print (smallest)
