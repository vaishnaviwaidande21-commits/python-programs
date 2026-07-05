for i in range(3):      #2                          # X O X
                                                   # O X O
    for j in range(3):  #2                        # X O X
          if((i+j) %2==0): 
            print("X", end = " ")
          else:
            print("O",end = " ")
    print()
