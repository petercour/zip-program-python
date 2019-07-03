# Basic zip program
# https://pythonprogramminglanguage.com/
import fire
import zipfile

class ZipApp(object):

    def create_zip(self, filename, yourfile):
        f = zipfile.ZipFile(filename,'w',zipfile.ZIP_DEFLATED)
        f.write(yourfile)
        f.close()


    def unzip(self,filename):
        zfile = zipfile.ZipFile(filename,'r')
        for filename in zfile.namelist():
            data = zfile.read(filename)
            file = open(filename, 'w+b')
            file.write(data)
            file.close()

if __name__ == '__main__':
    fire.Fire(ZipApp)
    
