def roman_numerals():
    total = 0
    response = str(input("Enter roman numeral in CAPS in descending order: ")) #This allow the user to enter the roman numeral to be tested
    
    Dictionary = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1} 
    while response != "":
        for number in response: #This statement goes through each number in the input 
            if number in Dictionary: 
                total = total + Dictionary[number]
        print (total)
        total = 0
        response = str(input("Enter roman numeral in CAPS in descending order: "))
roman_numerals()





