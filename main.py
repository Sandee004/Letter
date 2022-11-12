import emoji

'''
star = "*"
print((star+ "\n")*8)


#Letter L
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);



#Letter O
result_str="";   
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
				 

#Letter V
str="";    
for Row in range(0,7):    
    for Col in range(0,7):     
        if (((Col == 1 or Col == 5) and Row < 5) or (Row == 6 and Col == 3) or (Row == 5 and (Col == 2 or Col == 4))):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str); 


#Letter E
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);


#Letter U
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
'''

#Letter A
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 3 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);


#Letter Y
str=""
for Row in range(0,7):    
    for Col in range(0,7):     
        if (((Col == 1 or Col == 5) and Row < 2) or Row == Col and Col > 0 and Col < 4 or (Col == 4 and Row == 2) or ((Col == 3) and Row > 3)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str)		


#Letter O
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
			

print('''



''')
#Letter M
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str);


#Letter I
star = "*"
print((star+ "\n")*8)


#Conclusion
print(emoji.emojize("I wuv you Ayo and it's driving me crazy:confounded_face::red_heart:"))
