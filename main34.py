import os

def get_directory_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def calculateDirectorySize(folder, length):
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.islink(itempath): continue
        if os.path.isfile(itempath):
            fsize = os.path.getsize(itempath)
            fsizeperc =  100 * fsize / length
            print item.title(), ' size: ', fsize / 1024, 'KB ', fsizeperc, '%'
        elif os.path.isdir(itempath):
            dsize = get_directory_size(itempath)
            dsizeperc =  100 * dsize / length
            print item.title(), ' size: ', dsize / 1024, 'KB ', dsizeperc, '%'

folder = raw_input("What is the path?")
length = get_directory_size(folder)
print 'Total:', length / 1024, 'KB'
calculateDirectorySize(folder,length)
