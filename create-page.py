def readCurrentIndexFileToList():
    currentIndexFile = open ('index.html','r')
    currentIndexFileLines = []
    for line in currentIndexFile:
        currentIndexFileLines.append(line)
    currentIndexFile.close()
    return currentIndexFileLines

def generateOutputFileLines(currentIndexFileLines, numOpenFiles):
    outputFileLines = []
    currentPendingFiles = '<h3 id="recipe-2">Pending Files: '+str(numOpenFiles)+'</h3>'
    for line in currentIndexFileLines:
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
    currentIndexFileLines = readCurrentIndexFileToList()
    outputFileLines = generateOutputFileLines(currentIndexFileLines,numFiles)
    writeOutputFile(outputFileLines)
    
main()
