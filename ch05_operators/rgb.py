rgb = [255, 165, 13]
def format_rgb(rgb):
    rgb = ','.join(str(v) for v in rgb)
    #print(f'rgb({rgb})')
    return f'rgb({rgb})'
print(format_rgb(rgb))