

def RemoveChars(data_frame, column_name, replace, replace_with):
    data_frame[column_name] = data_frame[column_name].str.replace(replace,replace_with)
    return data_frame

