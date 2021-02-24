''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    pat_docs = input("Enter the number of patients & Docs seperated by docs").split(" ")
    for x in range(len(pat_docs)):
        pat_docs[x] = int(pat_docs[x])
    efforts = []
    for x in range(pat_docs[0]):
        y=[]
        y = input("Enter efforts by each doctor").split(" ")
        efforts.append(y)
    print(efforts)
    for x in range(pat_docs[1]):
        for y in range(pat_docs[0]):
            print(efforts[x][y])
            #efforts[x][y] = int(efforts[x][y])
    print(efforts)
main()



