# módulo de substituição de palavras em strings

'''
#prototipo em andamento (necessita de adaptacao para uso de case match)

def replace_word_in_text_1(txt,w,s):
    x = txt.find("hello")
    
    if(x == -1):
        print("[ERROR]: Selected word is not in text, returning original text")

    else:
        counter = 1
        while(1):
            y = txt.find(w,x+len(w),len(txt))
            if(y == -1):
                txt = txt.replace(w,s,counter)
                return txt
            x = y
            counter += 1
    return txt
'''


def substitui_palavra(texto,palavra_sub):
    return "Teste mock"
