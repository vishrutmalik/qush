from re import I
import sys
import ast

def generator(a,b):
    try:
        i=1
        while i<=a:
            if i%b==0:
                yield i
                i+=b
            else:
                i+=1
    finally:
        yield 0

def second(n):
    return [[j for j in range(1,i)] for i in range(2,n+2)]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Incorrect number of arguments,correct usage is\n"
              "\tpython3 gen_test.py {--generator}")
        raise ValueError

    elif len(sys.argv) == 3:
        if sys.argv[1] == "--second":
            print(second(int(sys.argv[2])))
        else:
            raise ValueError
            
    
    elif len(sys.argv) == 4:
        if sys.argv[1] == "--gen":
            print(sum(list(generator(int(sys.argv[2]),int(sys.argv[3])))))
        else:
            raise ValueError

    else:
        print(
            f"Incorrect number of arguments, expected 3/4 got {len(sys.argv)}")
        raise ValueError