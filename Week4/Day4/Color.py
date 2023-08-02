colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
def colorize(text, color):
    try:    
        if color not in colors:
            raise ValueError('Color not in tuple')
        if not isinstance(text,str):
            raise ValueError('Text not a string')
    except Exception as err:
        return err
    else:
        return 'Everything Ok'
print(colorize('Random Text', colors))