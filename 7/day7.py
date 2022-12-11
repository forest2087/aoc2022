import uuid

def uid():
    return str(uuid.uuid4().fields[-1])[:5]
    
def updateDirSize(dirs, dir_hierarchy, dir, size):
    # update curr dir
    if dir in dirs:
        dirs[dir]+=size
    else:
        dirs[dir]=size
    # print('update', dir, 'size')
    # search all parent folders and add size to them
    if dir!='/':
        parents = [a for a,b in dir_hierarchy if b==dir]
        # print('parents', parents)
        for parent in parents:
            dirs = updateDirSize(dirs, dir_hierarchy, parent, size)
    
    return dirs

def solv1(f):
    MOVE_IN = 1
    MOVE_OUT = 2
    MOVE_HOME = 3
    LIST_ = 4
    FILE = 5
    DIR = 6
    mode = 0
    dirs={}
    dir_hierarchy = []
    cur_dir=''

    # t = [[1, 3], [1, 4]]
    # print([a for a,b in t if b==4][0])

    # t = [["abc", "1239034 xyz"]]
    
    # print([b for a,b in t if a=='abc' and 'xyz' in b])
    
    i=0
    while True:
        ln = f.readline().strip()
        i+=1
        # if i==100:
        #     break
        if not ln:
            break;

        parts = ln.split()
        # command
        if parts[0]=='$': 
            
            if len(parts)==2:
                # list file
                mode = 4
            elif parts[1]=='cd':
                if parts[2]=='/':
                    # to home
                    mode = 3
                    cur_dir = '/'
                elif parts[2] == '..':
                    # out of a dir
                    mode = 2
                    if cur_dir!='/':
                        cur_dir = [a for a,b in dir_hierarchy if b==cur_dir][0]
                else:
                    # into a dir
                    mode = 1
                    # # add to relationship, no need, should already be there
                    # dir_hierarchy.append([cur_dir, part[2]])
                    # cur_dir = parts[2]

                    # find uid+dir
                    cur_dir = [b for a,b in dir_hierarchy if a==cur_dir and parts[2] in b][0]

        # file size
        else:
            if parts[0]=='dir':
                mode = 6
                dir_hierarchy.append([cur_dir, uid() + parts[1]])
            else:
                mode = 5
                dirs = updateDirSize(dirs, dir_hierarchy, cur_dir, int(parts[0]))
                
        # print(i, ln, cur_dir)    
        # print(dir_hierarchy)
    print(dir_hierarchy)
    print(dirs)
    print(sum([size for (dir, size) in dirs.items() if size<=100000]))
                

def solv2(f):
    
    MOVE_IN = 1
    MOVE_OUT = 2
    MOVE_HOME = 3
    LIST_ = 4
    FILE = 5
    DIR = 6
    mode = 0
    dirs={}
    dir_hierarchy = []
    cur_dir=''

    # t = [[1, 3], [1, 4]]
    # print([a for a,b in t if b==4][0])

    # t = [["abc", "1239034 xyz"]]
    
    # print([b for a,b in t if a=='abc' and 'xyz' in b])
    
    i=0
    while True:
        ln = f.readline().strip()
        i+=1
        # if i==100:
        #     break
        if not ln:
            break;

        parts = ln.split()
        # command
        if parts[0]=='$': 
            
            if len(parts)==2:
                # list file
                mode = 4
            elif parts[1]=='cd':
                if parts[2]=='/':
                    # to home
                    mode = 3
                    cur_dir = '/'
                elif parts[2] == '..':
                    # out of a dir
                    mode = 2
                    if cur_dir!='/':
                        cur_dir = [a for a,b in dir_hierarchy if b==cur_dir][0]
                else:
                    # into a dir
                    mode = 1
                    # # add to relationship, no need, should already be there
                    # dir_hierarchy.append([cur_dir, part[2]])
                    # cur_dir = parts[2]

                    # find uid+dir
                    cur_dir = [b for a,b in dir_hierarchy if a==cur_dir and parts[2] in b][0]

        # file size
        else:
            if parts[0]=='dir':
                mode = 6
                dir_hierarchy.append([cur_dir, uid() + parts[1]])
            else:
                mode = 5
                dirs = updateDirSize(dirs, dir_hierarchy, cur_dir, int(parts[0]))
                
        # print(i, ln, cur_dir)    
        # print(dir_hierarchy)
    # print(dir_hierarchy)
    # print(dirs)
    # print(sum([size for (dir, size) in dirs.items() if size<=100000]))

    unused = 70000000 - dirs['/']
    needed = 30000000 - unused
    size_list = sorted([b for a,b in dirs.items() if b>=needed])
    print(size_list)
    print(size_list[0])     
                