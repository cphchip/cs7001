# PDF Converter
# This program is to merge all assignments into a single PDF

from fileinput import close
from lib2to3.pgen2.token import RBRACE
import PyPDF2

# counter = 1

pdf1File = open('Assignment 1.1.py', 'r')
pdf2File = open('Assignment 1.2.py', 'r')
pdf3File = open('Assignment 1.3.py', 'r')
pdf4File = open('Assignment 1.4.py', 'r')
pdf5File = open('Assignment 1.5.py', 'r')
pdf6File = open('Assignment 1.6.py', 'r')
pdf7File = open('Assignment 1.7.py', 'r')
pdf8File = open('Assignment 1.8.py', 'r')
pdf9File = open('Assignment 1.9.py', 'r')
pdf10File = open('Assignment 1.10.py', 'r')
pdf11File = open('Assignment 1.11.py', 'r')
pdf12File = open('Assignment 1.12.py', 'r')
pdf13File = open('Assignment 1.13.py', 'r')
pdf14File = open('Assignment 1.14.py', 'r')
pdf15File = open('Assignment 1.15.py', 'r')
pdf16File = open('Assignment 1.16.py', 'r')
pdf17File = open('Assignment 1.17.py', 'r')
pdf18File = open('Assignment 1.18.py', 'r')
pdf19File = open('Assignment 1.19.py', 'r')
pdf20File = open('Assignment 1.20.py', 'r')

mergeFile = open('MergeFile.txt', 'a')
mergeFile.write(pdf1File)
mergeFile.write(pdf2File)
mergeFile.write(pdf3File)
mergeFile.write(pdf4File)
mergeFile.write(pdf5File)
mergeFile.write(pdf6File)
mergeFile.write(pdf7File)
mergeFile.write(pdf8File)
mergeFile.write(pdf9File)
mergeFile.write(pdf10File)
mergeFile.write(pdf11File)
mergeFile.write(pdf12File)
mergeFile.write(pdf13File)
mergeFile.write(pdf14File)
mergeFile.write(pdf15File)
mergeFile.write(pdf16File)
mergeFile.write(pdf17File)
mergeFile.write(pdf18File)
mergeFile.write(pdf19File)
mergeFile.write(pdf20File)

mergeFile.close()
pdf2File.close()
pdf3File.close()
pdf4File.close()
pdf5File.close()
pdf6File.close()
pdf7File.close()
pdf8File.close()
pdf9File.close()
pdf10File.close()
pdf11File.close()
pdf12File.close()
pdf13File.close()
pdf14File.close()
pdf15File.close()
pdf16File.close()
pdf17File.close()
pdf18File.close()
pdf20File.close()
pdf19File.close()