from git import Repo
repo = Repo('.')
print(repo)

#pass file object
def readTemplateToList(templateFile):

    templateFileLines = []
    for line in templateFile:
        templateFileLines.append(line)
    return templateFileLines

def generateOutputFileLines(templateFileLines, numOpenFiles):

    # empty array to output file lines
    outputFileLines = []

    currentPendingFiles = '<h3 id="recipe-2">Pending Files: '+str(numOpenFiles)+'</h3>'

    for line in templateFileLines:
        if ('<h3 id="recipe-2">' in line):
            line = currentPendingFiles
            outputFileLines.append(line)
        else:
            outputFileLines.append(line)

    return outputFileLines
    
def getNumFiles():
    numFilesFile = open('numFiles.txt','r')
    numFiles = numFilesFile.readline()
    numFilesFile.close()
    return int(numFiles)

def writeOutputFile(outputFileLines):

    outFile = open('index.html', 'w+')
    outFile.writelines(outputFileLines)
    outFile.close() 

def main():

    numFiles = getNumFiles()
    templateFile = open ('index.html','r')
    templateFileLines = readTemplateToList(templateFile)
    templateFile.close()
    outputFileLines = generateOutputFileLines(templateFileLines,numFiles)
    writeOutputFile(outputFileLines)
    

main()
