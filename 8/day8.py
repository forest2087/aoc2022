def getInput(f):
    trees = []
    while True:
        ln = f.readline().strip()
        if not ln: 
            break
        row = list(map(int, list(ln)))
        trees.append(row)
    R = len(trees)
    C = len(trees[0])
    edges = C*2+R*2-4
    # print(trees)
    # print(R, C)
    # print(edges)
    return [R, C, trees, edges]

# def solv1(f):
#     for i in range(10):
#         for j in range(10):
#             k = 10
#             while k>6:
#                 if k==7:
#                     break
#                 k-=1
#                 print(i, j, k)
#             if j==2:
#                 break
            
    
def solv1(f):
    R, C, trees, edges = getInput(f)
    
    # print(trees)
    # print(R, C)
    # print('edges', edges)
    cnt = edges
    
    for i in range(1, R-1):
        for j in range(1, C-1):
            
            # print('tree', i, j, trees[i][j])
            #check top
            di = i-1
            dj = j
            taller = 1
            while di>=0:
                if trees[i][j]<= trees[di][j]:
                    taller = 0
                    break
                di-=1
            if taller==1:
                cnt+=1
                continue
            
            
            di=i+1
            dj=j
            taller = 1
            while di<R:
                if trees[i][j]<= trees[di][j]:
                    taller = 0
                    break
                di+=1
            if taller==1:
                cnt+=1
                continue

            di=i
            dj=j-1
            taller = 1
            while dj>=0:
                if trees[i][j]<= trees[i][dj]:
                    taller = 0
                    break
                dj-=1
            if taller==1:
                cnt+=1
                continue

            di=i
            dj=j+1
            taller = 1
            while dj<C:
                if trees[i][j]<= trees[i][dj]:
                    taller = 0
                    break
                dj+=1
            if taller==1:
                cnt+=1
                continue

    print(cnt)
    return cnt

def solv2(f):
    R, C, trees, edges = getInput(f)

    cnt = 0
    for i in range(1, R-1):
        for j in range(1, C-1):
            # print('tree', i, j, trees[i][j])
            #check top
            di = i-1
            dj = j
            top=0
            while di>=0:
                if trees[di][j]<trees[i][j]:
                    top+=1
                elif trees[di][j]>=trees[i][j]:
                    top+=1
                    break
                    
                di-=1
            
            di=i+1
            dj=j
            bottom = 0
            while di<R:
                if trees[di][j]<trees[i][j]:
                    bottom+=1
                elif trees[di][j]>=trees[i][j]:
                    bottom+=1
                    break
                di+=1
            
            di=i
            dj=j-1
            left = 0
            while dj>=0 :
                if trees[i][dj]<trees[i][j]:
                    left+=1
                elif trees[i][dj]>=trees[i][j]:
                    left+=1
                    break
                dj-=1

            di=i
            dj=j+1
            right=0
            while dj<C :
                if trees[i][dj]<trees[i][j]:
                    right+=1
                elif trees[i][dj]>=trees[i][j]:
                    right+=1
                    break
                dj+=1
                
            cnt = max(cnt, top*bottom*left*right)            
            print(i, j, trees[i][j], ' -> ', top, left, bottom, right, ' -> ', top*bottom*left*right)
    print(trees)
    print(cnt)