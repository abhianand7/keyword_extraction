# first step - remove stop words
unique = set()
homedir = "/home/ubuntu/"
list_files = "files.txt"
new_file = homedir + "stopwords/" + "new.txt"
with open(homedir + list_files,'r') as fobj:
    ##obj = fobj.read().splitlines()
    with open(new_file,'w') as newfile:
        for line in fobj:
            line = line.strip()
            if '/' in line :
                dir = line
            else:
                ##print (line.rstrip('\n'))
                with open(dir + line,'r') as file:
                    for line in file:
                        line = line.strip()
                        if line not in unique:
                            unique.add(line)
                            newfile.write(line+'\n')
                            
print (set(unique))