#slicing
l1 = [10, 20, 30, 40, 50, 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(l1)):
  print(i, l1[i], i-len(l1))

l1[9] = 80 
l1 #list is mutable

#nested lists
le = [10, [20]]
le[1][0]

new_l = [10, ['Apple', 'Banana']]
new_l2 = [10, 'apple', 'banana']
len(new_l), len(new_l2)

#indexing nested lists
l3 = [10, 20, ['Apple', 'Banana', 'Cherry']]
l3[2][2]

l5=['Apple',['kashmir',['India',['Mumbai',['MH',['Shivaji',['Shambaji',['Viky']]]]]]]]
len(l5)
l5[1][1][1][1][1][1][1][0]
l6 = [[[[[[[[['Apple']]]]]]]]]
l6[0][0][0][0][0][0][0][0][0]
