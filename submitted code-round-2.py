



''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def main():
  ntc = 0
  ntc = int(input(""))
  condi = lambda a1,a2: set(a1).union(set(a2))
  for x in range(ntc):
    sot = int(input(""))
    a1=input("").split()
    a1 = sorted(list(map(int,a1)),reverse=True)
    b1=input("").split()
    b1 = sorted(list(map(int,b1)),reverse=True)  
    c1=[]


    for x in a1:
      for y in b1:
        if (x>y):
          c1.append([x,y])
          b1.remove(y)
          break
        else:
          continue

    print(len(c1))
    #print(c1)

main()


