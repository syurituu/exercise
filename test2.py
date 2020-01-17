import jieba

def splitfile(inputFile, outputFile):
    fin=open(inputFile,'r',errors='ignore')
    fout=open(outputFile,'w',errors='ignore')
    for line in fin:
        line = line.strip()
        line = jieba.cut(line)
        outstr = " ".join(line)
        fout.write(outstr + '\n')
    fin.close()
    fout.close()

splitfile('msr_test.txt','result2.txt')