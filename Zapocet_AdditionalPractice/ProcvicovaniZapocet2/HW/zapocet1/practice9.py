import sys
import os

def statusReader(file: str, status: str) -> int:
    count = 0
    with open(file, "r",encoding="utf-8") as f:
        for line in f:
            if status.lower() in line.split(":")[0].lower():
                count+=1
    return count

def statusExtractor(file: str, status: str, output: str) -> None:
    linesToExtract = []
    with open(file, "r",encoding="utf-8") as f:
        for line in f:
            if status.lower() in line.split(":")[0].lower():
                linesToExtract.append(line.strip())
    with open(output,"w",encoding="utf-8") as f:
        for line in linesToExtract:
            f.write(f"{line}\n")

#statusExtractor ale s dual open files:
"""
def statusExtractor(file: str, status: str, output: str) -> None:
    # Open both files: 'r' for reading, 'w' for writing
    with open(file, "r", encoding="utf-8") as fin, \
         open(output, "w", encoding="utf-8") as fout:
        
        for line in fin:
            if status.lower() in line.split(":")[0].lower():
                fout.write(line) # line already has \n from the source
"""

def main():
    if len(sys.argv)<3:
        print("Usage: python analyzer.py <input_file> <status> [output_file]")
        sys.exit(1)
    fileToRead = sys.argv[1]
    status = sys.argv[2]
    if os.path.exists(fileToRead):
        if len(sys.argv) == 3:
            print(f"Status type \"{status}\" has occured {statusReader(fileToRead,status)} times.")
        else:
            fileToOutput = sys.argv[3]
            print(f"Status type \"{status}\" has occured {statusReader(fileToRead,status)} times.")
            statusExtractor(fileToRead,status,fileToOutput)
    else:
        print("The file does not exist.")
    
            
if __name__ == '__main__':
    main()