from itu.algs4.fundamentals.uf import UF
from itu.algs4.stdlib.stdio import readInt

# Operation: 0
# def query( ) checks if s and t belongs to the same set either S or T.
# I use the UF library to instantiate uf. Then I call the method .find( ) from UF as a helper method.
def query(uf, s, t):
    parent_s = uf.find(s)
    parent_t = uf.find(t)

    # If S = T it means that s and t belongs to the same set, and then 1 is printed
    if parent_s == parent_t:
        print(1)
    # If S != T, then s and t do not belong to the same set, and then 0 is printed
    else: 
        print (0)
        

# Operation: 1
# def union( ) unionize the two sets S and T (S U T) if S != T (uf.union( ) uses .fin( ) as a helper method).
# If S = T then nothing happpens, because then s and t is already in the same set
def union(uf, s, t):
    uf.union(s, t)

# Operation: 2
# def move( ) moves element s from S til T if S != T
# It removes s from S and adds s to T by TUs 
# def move(uf, s, t):
#     parent_s = uf.find(s)
#     parent_t = uf.find(t)

#     # If S != T then s must be moved to T
#     if parent_s != parent_t:
#         parent_s - s
#         parent_t + s


def main():
    # n number of singletons (sets with one element), which is the first integer in the input.
    n = readInt()

    # uf is an instantiazation of the library UF passed with the parameter n which declares how many singleton sets there must be produced.
    uf = UF(n)

    # m number of lines of the form "0 s t" or "1 s t" or "2 s t".
    m = readInt()

    # While there is more than 0 lines left in the input the program performs the given operation (operation 0, 1 or 2) that is declared in the given line.
    while (m > 0):
        operation = readInt()
        s = readInt()
        t = readInt()

        # If operation == 0, then the def query( ) is called and initialized on our uf instance.
        # The instance is passed with the parameters s and t representing elements in a singleton set.
        if (operation == 0):
            query(uf, s, t)

        # If operation == 1, then the def union( ) is called and initialized on our uf instance.
        # The instance is passed with the parameters s and t representing elements in a singleton set.
        if(operation == 1):
            union(uf, s, t)

        # If operation == 2, then the def move( ) is called and initialized on our uf instance.
        # The instance is passed with the parameters s and t representing elements in a singleton set.
        # if(operation == 2):
        #     move(uf, s, t)
        
        # When an operation has been performed on a line, the program discard the given line and moves onto next line until theres 0 lines left to check.
        m -=1


# End every .py file with this.
if __name__ == "__main__":
    main()