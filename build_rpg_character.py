full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):

    if isinstance(name,str)==False:
        return 'The character name should be a string'
    
    elif name=='':
        return 'The character should have a name'
    
    elif len(name)>10:
        return 'The character name is too long'
    
    elif ' ' in name:
        return 'The character name should not contain spaces'
    
    elif isinstance(strength,int)==False or isinstance(intelligence, int)==False or isinstance(charisma,int)==False:
        return 'All stats should be integers'
    
    elif strength<1 or intelligence<1 or charisma<1:
        return 'All stats should be no less than 1'
    
    elif strength>4 or intelligence>4 or charisma>4:
        return 'All stats should be no more than 4'
    
    elif strength + intelligence + charisma !=7:
        return 'The character should start with 7 points'
    
    else:
        strength_dot = full_dot*strength
        strength_edot = empty_dot * (10-strength)
        stren= strength_dot + strength_edot

        int_dot = '●'*intelligence
        int_edot = '○' * (10-intelligence)
        intel = int_dot + int_edot

        cha_dot = '●'*charisma
        cha_edot = '○' * (10-charisma)
        cha = cha_dot + cha_edot
        return f'{name}\nSTR {stren}\nINT {intel}\nCHA {cha}'

final=create_character('ren', 4, 2, 1)
print(final)