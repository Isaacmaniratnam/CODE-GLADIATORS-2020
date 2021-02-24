'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    N=0
    list1= []
    list2 = []
    list3 = []
    while(N<=0 or N>= 10000000):
        N= int(input("Enter Number of Ingredients\t"))
    while (len(list1)<N or int(max(list1))> 2**63-1 or int(min(list1)) < 0 ):
        req_qty= input("Req Qty\t")
        list1 = req_qty.split()
        print(list1)
    while (len(list2)!=N or int(max(list2))> 2**63-1 or int(min(list2)) < 0  ):
        present_qty= input("Present Qty\t")
        list2 = present_qty.split()
        print(list2)
    for x,y in zip(list1,list2):
        list3.append(int(y)/int(x))
    print(list3)
    print(int(min(list3)))
    
main()

