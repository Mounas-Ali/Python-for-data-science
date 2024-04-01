def     NULL_not_found(object: any) -> int:
    
    if object == None:
        print(f"Nothing: {(object)} {type(object)}")
        return 0     
    elif Flooat(object):
        print(f"Cheese: {(object)} {type(object)}")
        return 0
    elif object == int:
        print(f"Zero: {(object)} {type(object)}")
        return 0
    elif object == '':
        print(f"Empty: {(object)} {type(object)}")
        return 0
    elif object == False:
        print(f"Fake: {(object)} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1

def Flooat(nbr):
     return nbr != nbr