def dif_mat():
    t=[]
    m=[]
    M=[]
    def matrice_a():
        print("ENTER YOUR MAT-A")
        def Initialize_Board():
            t.clear()
            for i in range(9):
                t.append('-')
        Initialize_Board()
        def Display_Board():
            for i in range(9):
                print(t[i], '[', i+1, '] \t', end='')
                if (i+1)%3 == 0:
                    print("\n")
        def input_data():
            count=0
            while count<9:
                data=int(input("please enter the number(A):"))
                t[count]=data
                count=count+1
                if count<9:
                    Display_Board()
        input_data()
        print("A_MAT:"),Display_Board()
    def matrice_b():  
        print("ENTER YOUR MAT-B")      
        def Initialize_Board():
            m.clear()
            for i in range(9):
                m.append('-')
        Initialize_Board()
        def Display_Board():
            for i in range(9):
                print(m[i], '[', i+1, '] \t', end='')
                if (i+1)%3 == 0:
                    print("\n")
        def input_data():
            count=0
            while count<9:
                data=int(input("please enter the number(B):"))
                m[count]=data
                count=count+1
                if count<9:
                    Display_Board()
        input_data()
        print("B_MAT:"),Display_Board()
    def matrice_ans():        
        def Initialize_Board():
            M.clear()
            for i in range(9):
                M.append('-')
        Initialize_Board()
        def Display_Board():
            for i in range(9):
                print(M[i], '[', i+1, '] \t', end='')
                if (i+1)%3 == 0:
                    print("\n")
        def input_data():
            data=t[0]*m[0]+t[1]*m[3]+t[2]*m[6]
            M[0]=data
            data=t[0]*m[1]+t[1]*m[4]+t[2]*m[7]
            M[1]=data
            data=t[0]*m[2]+t[1]*m[5]+t[2]*m[8]
            M[2]=data
            data=t[3]*m[0]+t[4]*m[3]+t[5]*m[6]
            M[3]=data
            data=t[3]*m[1]+t[4]*m[4]+t[5]*m[7]
            M[4]=data
            data=t[3]*m[2]+t[4]*m[5]+t[5]*m[8]
            M[5]=data
            data=t[6]*m[0]+t[7]*m[3]+t[8]*m[6]
            M[6]=data
            data=t[6]*m[1]+t[7]*m[4]+t[8]*m[7]
            M[7]=data
            data=t[6]*m[2]+t[7]*m[5]+t[8]*m[8]
            M[8]=data
        input_data()
        print("ANS_MAT:"),Display_Board()
    
    matrice_a()
    matrice_b()
    matrice_ans()
def sqr_mat():
    t=[]
    m=[]
    M=[]
    def matrice_a():
        print("ENTER YOUR MAT-A")
        def Initialize_Board():
            t.clear()
            for i in range(9):
                t.append('-')
        Initialize_Board()
        def Display_Board():
            for i in range(9):
                print(t[i], '[', i+1, '] \t', end='')
                if (i+1)%3 == 0:
                    print("\n")
        def input_data():
            count=0
            while count<9:
                data=int(input("please enter the number(A):"))
                t[count]=data
                count=count+1
                if count<9:
                    Display_Board()
        input_data()
        print("A_MAT:"),Display_Board()
    def matrice_ans():        
        def Initialize_Board():
            M.clear()
            for i in range(9):
                M.append('-')
        Initialize_Board()
        def Display_Board():
            for i in range(9):
                print(M[i], '[', i+1, '] \t', end='')
                if (i+1)%3 == 0:
                    print("\n")
        def data_ans():
            data=t[0]*t[0]+t[1]*t[3]+t[2]*t[6]
            M[0]=data
            data=t[0]*t[1]+t[1]*t[4]+t[2]*t[7]
            M[1]=data
            data=t[0]*t[2]+t[1]*t[5]+t[2]*t[8]
            M[2]=data
            data=t[3]*t[0]+t[4]*t[3]+t[5]*t[6]
            M[3]=data
            data=t[3]*t[1]+t[4]*t[4]+t[5]*t[7]
            M[4]=data
            data=t[3]*t[2]+t[4]*t[5]+t[5]*t[8]
            M[5]=data
            data=t[6]*t[0]+t[7]*t[3]+t[8]*t[6]
            M[6]=data
            data=t[6]*t[1]+t[7]*t[4]+t[8]*t[7]
            M[7]=data
            data=t[6]*t[2]+t[7]*t[5]+t[8]*t[8]
            M[8]=data
        data_ans()
        print("ANS_MAT:"),Display_Board()
    matrice_a()
    matrice_ans()
    
sqr_mat()