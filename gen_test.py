import sys
import ast

def fib():
    mem=[1,1]
    c=0
    s=0
    i=2
    while(c<100):
        mem.append(mem[i-1]+mem[i-2])
        if mem[i]%2==0: 
            c+=1
            s+=mem[i]
        i+=1
    return s

def merge(l1,l2):
    l3=[]
    cm=set()
    i=0
    j=0
    while(i<len(l1) and j<len(l2)):
        if l1[i]<l2[j]:
            i+=1
        elif l2[j]<l1[i]:
            j+=1
        else:
            if l1[i] not in cm:
                l3.append(l1[i])
                cm.add(l1[i])
            i+=1
            j+=1
    
    
    return l3

def allEven(x):
    return set(str(x)).issubset(set("02468"))

    
def eval(x):
    s=str(x)
    a,b,c,d=s, s+s, s+s+s, s+s+s+s
    return (int(a)+int(b)+int(c)+int(d))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Incorrect number of arguments,correct usage is\n"
              "\tpython3 gen_test.py {--fib}")
        raise ValueError

    elif len(sys.argv) == 2:
        if sys.argv[1] == "--fib":
            print(fib())

        else:
            print("Correct usage is python3 gen_test.py {--fib}")
            raise ValueError
            
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--checkEven":
            print(allEven(sys.argv[2]))
        elif sys.argv[1] == "--eval":
            print(eval(sys.argv[2]))
        else:
            print("Correct usage is python3 gen_test.py {--checkEven} {--eval}")
            raise ValueError
    
    elif len(sys.argv)==4 and sys.argv[1] == "--merge":
        l1=ast.literal_eval(sys.argv[2])
        l2 = ast.literal_eval(sys.argv[3])
        print(merge(l1,l2))

    else:
        print(
            f"Incorrect number of arguments or format, expected 2/3/4 got {len(sys.argv)}")
        raise ValueError
