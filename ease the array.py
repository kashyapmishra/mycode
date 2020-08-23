Given an array of integers of size N. Assume ‘0’ as invalid number and all other as valid number. Write a program that modifies the array in such a way that if next number is
valid number and is same as current number, double the current number value and replace the next number with 0. After the modification, rearrange the array such that all 0’s
are shifted to the end and the sequence of the valid number or new doubled number is maintained as in the original array.
Examples:

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test case follows. First line of each test contains an integer N denoting 
the size of the array. Then next line contains N space separated integers denoting the elements of the array.

Output:
For each test case print space separated elements of the new modified array on a new line.
code


a=[0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
for i in range(len(a)-1):
    if a[i]!=0 and a[i]==a[i+1]:
        a[i]=2*a[i]
        a[i+1]=0
b=[]
for i in a:
    if i!=0:
        b.append(i)
b=b+[0]*(len(a)-len(b))
print(b)


output
[4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
