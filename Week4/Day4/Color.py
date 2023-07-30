def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    try:    
        if color not in colors:
            raise ValueError('Color not in tuple')
        if not isinstance(text,str):
            raise ValueError('Text not a string')
    except Exception as err:
        print(err)
    else:
        print('Everything Ok')
    return
