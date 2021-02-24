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

    for line in templateFileLines:
        if ("#var2" in line):
            line = line.replace('#var2',str(numOpenFiles))
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

def gitPush():
    try:
        repo = Repo('.')
        repo.git.add(update=True)
        repo.index.commit('COMMIT_MESSAGE')
        origin = repo.remote('origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')  

def main():

    #get the number of files from numFiles.txt
    numFiles = getNumFiles()

    #get template file
    templateFile = open ('template.html','r')

    #get template file lines
    templateFileLines = readTemplateToList(templateFile)

    #close template file
    templateFile.close()

    #generate output file lines
    outputFileLines = generateOutputFileLines(templateFileLines,numFiles)

    #write file to index file
    writeOutputFile(outputFileLines)
    
    gitPush()

main()
