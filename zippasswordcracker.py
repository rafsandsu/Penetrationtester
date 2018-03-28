#python program to crack paswords for zip file

import zipfile
import optparse
from threading import Thread

def extract(zipfile, password):
    try:
        zipfile.extractall(pwd=password)
        print '[+] Found password ' + password + '\n'
    except:
        pass
def main():
    parser = optparse.OptionParser("usage%prog "+\
            "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zip', type='string',\
            help='specify zip file')
    parser.add_option('-d', dest='dict', type='string',\
            help='speficy dictionary file')
    (options, args) = parser.parse_args()
    if (options.zip == None) | (options.dict == None):
        print parser.usage
        exit(0)
    else:
        zipname = options.zip
        dictionaryname = options.dict
    Zfile = zipfile.ZipFile(zipname)
    passfile = open(dictionaryname)
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract, args=(Zfile, password))
        t.start()
if __name__ == '__main__':
    main()
