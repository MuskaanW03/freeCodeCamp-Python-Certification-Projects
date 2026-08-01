def number_pattern(n):
    pattern = ''
    if isinstance(n,int)==False:
            return 'Argument must be an integer value.'
        
    elif n<1:
        return 'Argument must be an integer greater than 0.'
        
    else:
        for i in range(1,n+1):
            num=str(i)
            pattern += num + ' '