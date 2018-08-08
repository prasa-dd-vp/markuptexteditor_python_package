import re

def home(request):
    return render(request, 'app/index.html')

def bold(data):
    #print("inside bold"+data)
    return re.sub(r'\*\*([_/a-zA-Z0-9\\__,.\s]+)\*\*',r'<b>\1</b>',data)

def italics(data):
    #print("inside italics"+data)
    return re.sub(r'//([<a-z>]*)([^:][a-zA-Z\_,.\s]+)([/<a-z>]*)//',r'<i>\1\2\3</i>',data)

def underline(data):
    #print("inside underline"+data)
    return re.sub(r'__([<a-z>]*)([a-zA-Z\\__,.\s]+)([/<a-z>]*)__',r'<u>\1\2\3</u>',data)

def strike(data):
    #print("inside underline"+data)
    return re.sub(r'\$\$([<a-z>]*)([a-zA-Z\\__,.\s]+)([/<a-z>]*)\$\$',r'<strike>\1\2\3</strike>',data)

def newline(data):
    return re.sub(r'([\n]+)',r'\1<br>',data) 

def bullets(data):
    #print("inside bullets "+data)
    b = re.sub(r'\s{1}\*{1}\s{1}(.*)\n',r'<ul><li>\1</li></ul>',data)
    b = b.replace("</ul><br><ul>","")
    b = b.replace("</ul><br>","</ul>")
    return b

def numbers(data):
    #print("inside fun"+ data)
    n = re.sub(r'\s{1}[0-9]+.{1}\s{1}(.*)\n',r'<ol><li>\1</li></ol>',data)
    #print(n)
    n = n.replace("</ol><br><ol>","")
    n = n.replace("</ol><br>","</ol>")
    return n

def link(data):
    return re.sub(r'\[(\w+)\]\(([\w:/.]+)\)',r'<a href= "\2">\1</a>',data)
