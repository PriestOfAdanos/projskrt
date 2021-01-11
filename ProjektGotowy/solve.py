import os


## global 

tree_size, flie_count, save_failures,boy_dat, girl_dat = 0, 0, 0, 0, 0

def brute(data):
    # method appends to list every possible path for both boy and girl on a directional 
    # graph and than compares them to find commony aprchablle nodes. It returns numbers 
    # of steeps needed to reach said node for (boy,girl) with shortest path. In case of
    # multiple fitting solutions it returns the one in which girl has to scale the shortest path. 

    tree = data[1]
    for para in range(2, data[0][1]+2):

        #boy
        current_node = data[para][0]-1
        aproachable = dict()
        for i in range(data[0][0]):
            if current_node+1 in aproachable:
                current_node = tree[current_node]-1
                continue
            aproachable[current_node+1]=i
            current_node = tree[current_node]-1

        #girl
        current_node = data[para][1]-1
        aproachable2 = dict()
        for i in range(data[0][0]):
            if current_node+1 in aproachable2:
                current_node = tree[current_node]-1
                continue
            aproachable2[current_node+1]=i
            current_node = tree[current_node]-1

        #common nodes
        combine = {}
        for i in aproachable.keys():
            try:
                combine[(aproachable[i],aproachable2[i])] = (aproachable2[i]**5+aproachable[i]**5)-(aproachable2[i]<aproachable[i]) 
            except KeyError:
                pass # in case keys do not match 
        try:
            return min(combine, key=combine.get)
        except:
            return '(-1,-1)'

### helpres 


def data_miner(f):
    parsed_data=[]
    for line in f.readlines():
        parsed_data.append(line.rstrip().split(" "))
    for i in range(len(parsed_data)):
        for j in range(len(parsed_data[i])):
            parsed_data[i][j] = int(parsed_data[i][j])
    return parsed_data



try:
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), "input")):
        with open(os.path.join(os.path.dirname(__file__),"input", filename), 'r') as f:
                try:
                    
                    file_out = open(os.path.join(os.path.dirname(__file__), "output","output_{}.txt".format(filename)), "w")
                    data = data_miner(f)
                    cst = brute(data)
                    file_out.writelines(str(cst))
                    file_out.close()
                    flie_count+=1
                    girl_dat += cst[1]
                    boy_dat += cst[0]
                    tree_size+=data[0][0]
                except IOError:
                    save_failures+=1
                    file_out = open("failed_files.txt", "a")
                    file_out.writelines("błąd zapisu danych dla danych z przetwarzania pliku {}".format(filename))
                    file_out.close()
except:
    exit(0)
file_out = open("raport.txt", "w")
file_out.writelines("Processed files: \n{}\nFailed files\n{}\nBoy avg:\n{}\nGirl data\n{}\nTree size\n{}".format(flie_count,save_failures,boy_dat, girl_dat,tree_size))
file_out.close()
exit(1)
