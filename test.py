import jieba

def readFile(path):
    with open(path,'r',errors='ignore') as file:
        content = file.read()
        return content
def saveFile(path,result,errors='ignore'):
    with open(path,'w') as file:
        file.write(result)

content = readFile("C:/Users/Tom/Desktop/jieba/pku_test.txt")
cutResult = jieba.cut(content)
saveFile("C:/Users/Tom/Desktop/jieba/result.txt"," ".join(cutResult))