test_settings={
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}

def add_setting(test_settings, keyValue):
    key,value = keyValue
    lower_key= key.lower()
    lower_value = value.lower()

    if lower_key in test_settings.keys():
        return f"Setting '{lower_key}' already exists! Cannot add a new setting with this name."
    
    else:
        test_settings.update({lower_key:lower_value})
        return f"Setting '{lower_key}' added with value '{lower_value}' successfully!"

def update_setting(test_settings, keyValue):
    key,value = keyValue
    lower_key= key.lower()
    lower_value = value.lower()

    if lower_key in test_settings.keys():
        test_settings.update({lower_key:lower_value})
        return f"Setting '{lower_key}' updated to '{lower_value}' successfully!"
    
    else:
        return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):
    lower_key = key.lower()
    

    if lower_key in test_settings.keys():
        test_settings.pop(lower_key)
        return f"Setting '{lower_key}' deleted successfully!"
    
    else:
        return 'Setting not found!'

def view_settings(test_settings):
    if test_settings == dict():
        return 'No settings available.'
    
    elif test_settings !={}:
        dict_list=[]
        for key,value in test_settings.items():
            new_key = key.capitalize()
            dict_list.append(f'{new_key}: {value}\n')
            new_dict_list = ''.join(dict_list)
        return f"Current User Settings:\n{new_dict_list}"

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) )