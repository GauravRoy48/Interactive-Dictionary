import json
# https://docs.python.org/3/library/index.html
from difflib import get_close_matches

errormsg = "\nThe word is not available in my database! Please double check the word or search somewhere else."

#---------------------Function definition start-------------------------------
def meaning(w,error):
    if w in data:
        print('\n'+str(w)+' :')
        return data[w]
    
    elif w.title() in data:
        print('\n'+str(w.title())+' :')
        return data[w.title()]
    
    elif w.lower() in data:
        print('\n'+str(w.lower())+' :')
        return data[w.lower()]
    
    elif w.upper() in data:
        print('\n'+str(w.upper())+' :')
        return data[w.upper()]
    
    elif len(get_close_matches(w,data.keys()))>0 or len(get_close_matches(w.lower(),data.keys()))>0 or len(get_close_matches(w.upper(),data.keys()))>0:
        if len(get_close_matches(w,data.keys()))>0:
            decision = input("Did you mean %s (y or n): " %get_close_matches(w,data.keys())[0])         
            if decision == 'y' or decision =='Y':
                print('\n'+str(get_close_matches(w,data.keys())[0])+' :')
                return data[get_close_matches(w,data.keys())[0]]
            elif len(get_close_matches(w.lower(),data.keys()))>0:
                decision = input("Did you mean %s (y or n): " %get_close_matches(w.lower(),data.keys())[0])             
                if decision == 'y' or decision =='Y':
                    print('\n'+str(get_close_matches(w.lower(),data.keys())[0])+' :')
                    return data[get_close_matches(w.lower(),data.keys())[0]]
                elif len(get_close_matches(w.upper(),data.keys()))>0:
                    decision = input("Did you mean %s (y or n): " %get_close_matches(w.upper(),data.keys())[0])                  
                    if decision == 'y' or decision =='Y':
                        print('\n'+str(get_close_matches(w.upper(),data.keys())[0])+' :')
                        return data[get_close_matches(w.upper(),data.keys())[0]]
                    else:
                        return error
        elif len(get_close_matches(w.lower(),data.keys()))>0:
            decision = input("Did you mean %s (y or n): " %get_close_matches(w.lower(),data.keys())[0])
            if decision == 'y' or decision =='Y':
                print('\n'+str(get_close_matches(w.lower(),data.keys())[0])+' :')
                return data[get_close_matches(w.lower(),data.keys())[0]]
            elif len(get_close_matches(w.upper(),data.keys()))>0:
                decision = input("Did you mean %s (y or n): " %get_close_matches(w.upper(),data.keys())[0])            
                if decision == 'y' or decision =='Y':
                    print('\n'+str(get_close_matches(w.upper(),data.keys())[0])+' :')
                    return data[get_close_matches(w.upper(),data.keys())[0]]
                else:
                    return error
        elif len(get_close_matches(w.upper(),data.keys()))>0:
            decision = input("Did you mean %s (y or n): " %get_close_matches(w.upper(),data.keys())[0])
            if decision == 'y' or decision =='Y':
                print('\n'+str(get_close_matches(w.upper(),data.keys())[0])+' :')
                return data[get_close_matches(w.upper(),data.keys())[0]]
            else:
                return error
            
    else:
        return error
#---------------------Function definition end-------------------------------

data = json.load(open("data.json"))
keepgoing = True

print('\n\nWelcome to My Dictionary program!')

while keepgoing:
    word = input('Enter word: ')
    res = meaning(word,errormsg)
    
    if res is None:
        res = errormsg
    elif type(res)==list:
        res_new = ""
        for item in res:
            item = '-'+str(item)
            res_new = res_new + item+'\n'
        res = res_new
    elif res != errormsg:
        res = '-'+str(res)
        
    print(res)
    
    q = input('Would you like to search another word (y or n): ')
    if q!='y' and q!='Y':
        keepgoing = False
        
print("\nBye!\n")
