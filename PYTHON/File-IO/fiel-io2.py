with open('book.csv') as f :  
    rows = f.readlines()  
    isFirstLine = True
    for r in rows :  
        if isFirstLine :
            isFirstLine = False  
            continue
        cols = r.split(',')
        print('Student Name = ', cols[0], end=" ")  
        print('\tEn. No. = ', cols[1], end=" ")  
        print('\tCPI = \t', cols[2])