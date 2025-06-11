longtext = "Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu."
query = "síň"

surroundings = 7

if query in longtext:
    text_before = longtext.split(query)[0]
    text_after = longtext.split(query)[1]
    
    print()
    print(query)
    print()

