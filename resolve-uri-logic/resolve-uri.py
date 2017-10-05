import urllib.parse

def decode_url(location):
    loc = location[1:]
    length = len(loc)       
    rows = int(location[0]) 
    mod = length % rows      
    baseCol = length // rows 

    l = []
    for row in range(rows):
        if row < mod:
            ln = baseCol + 1
        else:
            ln = baseCol
        l.append(loc[:ln])
        loc = loc[ln:]

    dURL = ''
    for n in range(length):
        dURL += l[n%rows][n//rows]
    return urllib.parse.unquote(dURL).replace('^', '0')

# location = "7h%md2F22285Emu%%8f63%%5nt25nF5F1F179pt35ca1255EutF..987216%23hDE34cbEE-lp%ac19%67451%_7636cd5%%l%2lo515279E_3k2%312-3553Fim%5E53_%lFe5577b15EEAoc%2%9%415.ayeEd9558%-"
# print(decode_url(location))