files = []
totalSize = 0

with open('input.txt','r') as f:
    for l in f:
        
        files.append(l.strip())

path = "/main"
dirs = {"/main":0}

for command in files:
    
    if command[0] == "$":
        if command [2:4] == "ls":
            pass
        elif command[2:4] == "cd":
        
            if command [5:6] == "/": ##if its cd / means its base dir
                path = "/main"
                    
            elif command [5:7] == "..":
                path = path[:path.rfind("/")]
            
            else:
                dir_name = command[5:]
                path = path + "/" + dir_name
                dirs.update({path:0})
                
    elif command[0:3] == "dir":
        pass
    
    else:
        size = int(command[:command.find(" ")])
        
        dir = path
        
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]
            
for i in dirs:
    if dirs[i] <100001:
        totalSize += dirs[i]
        
print (totalSize)

# end of part 1
################
limit = 30000000 - (70000000 - dirs["/main"])
valid_dirs = []
for i in dirs:
    if limit <= dirs[i]:
        valid_dirs.append(dirs[i])
        
    smallest = min(valid_dirs)

print(smallest)
# end of part 2