import random
#物品重量和价格，可由自己规定
X={1:[10,15],2:[15,25],3:[20,35],4:[25,45],5:[30,55],6:[35,40],7:[20,30],8:[23,42],9:[33,76]}
#终止界限
FINISHED_LIMIT=1
#重量界限，即背包所能承载的重量上限
WEIGHT_LIMIT=80
#染色体长度
CHROMOSOME_SIZE=6
#遴选次数，详情见1.2.3
SELECT_NUMBER=100
max_last=0
diff_last=10000
#最优个体
BEST=['000000',[0,0]]
#随机生成染色体样态
def randomChromosomeState():
    chromosome_state=''
#因为倾向于放置3个以上的物品，所以这里初始染色体样态选择0.6的概率为1，0.4的概率为0。
    for i in range(CHROMOSOME_SIZE):
        if random.random()<0.6:
            chromosome_state+='1'
        else:
            chromosome_state+='0'
    return chromosome_state
#初始化函数
def init():
    chromosome_states=[]
    for i in range(SELECT_NUMBER):
        chromosome_states.append(randomChromosomeState())
    return chromosome_states
#计算适应度
def fitness(chromosome_states):
    fitnesses=[]
    for chromosome_state in chromosome_states:
        value_sum=0
        weight_sum=0
        for i,v in enumerate(chromosome_state):
            if int(v)==1:
                weight_sum+=X[i+1][0]
                value_sum+=X[i+1][1]
        fitnesses.append([value_sum,weight_sum])
    return fitnesses
#筛选函数
def fiter(chromosome_states,fitnesses):
    global BEST
    #重量大于80的被淘汰
    index=len(fitnesses)
    while index>=1:
        index-=1
        if fitnesses[index][1]>WEIGHT_LIMIT:
            chromosome_states.pop(index)
            fitnesses.pop(index)
        else:
            if fitnesses[index][0]>BEST[1][0]:
                BEST[0]=chromosome_states[index]
                BEST[1]=fitnesses[index]
 #遴选
    select_index=[0]*len(chromosome_states)
    possibles=possibility(fitnesses)
    for i in range(SELECT_NUMBER):
        j=select(random.random(),possibles)
        select_index[j]+=1
    return select_index
#计算繁殖概率
def possibility(fitnesses):
    possibles=[]
    value_sum=0
    for fitness in fitnesses:
        value_sum+=fitness[0]*fitness[0]*fitness[0]*fitness[0]
    for fitness in fitnesses:
        possibles.append(fitness[0]*fitness[0]*fitness[0]*fitness[0]/value_sum)
    for i in range(1,len(possibles)):
        possibles[i]=possibles[i]+possibles[i-1]#累加每个概率，使每个概率区间对应一个染色体的选择概率
    return possibles
#遴选繁殖个体
def select(possible,possibles):
    for index in range(0,len(possibles)):
        if possible<possibles[index]:
            return index
#交叉互换的实现
def crossover(chromosome_states,select_index):
    chromosome_states_new=[]
    index=len(chromosome_states)
    while index>=1:
        index-=1
        chromosome_state=chromosome_states.pop(index)
        for i in range(select_index[index]):
            chromosome_state_x=random.choice(chromosome_states)
            pos=random.choice(range(1,CHROMOSOME_SIZE-1))
            cp=random.random()#引入重组率
            if cp >0.5:
                chromosome_states_new.append(chromosome_state[:pos]+chromosome_state_x[pos:])
            else:
                chromosome_states_new.append(chromosome_state)
        chromosome_states.insert(index,chromosome_state)
    return chromosome_states_new
#单点变异的实现过程
def mutation(chromosome_states_new):
    for chr in chromosome_states_new:
        mp=random.random()#引入变异率
        if mp>0.9:
            pos=random.choice(range(0,CHROMOSOME_SIZE-1))
            lchr=list(chr)
            lchr[pos]=str(1-int(chr[pos]))
            chr=''.join(lchr)
    return chromosome_states_new
#收敛条件判断
def is_finished(fitnesses):
    global max_last
    global diff_last
    max_current=0
    for v in fitnesses:
        if v[0]>max_current:
            max_current=v[0]
    diff=max_current-max_last
#连续两代适应度无变化时停止迭代
    if diff<FINISHED_LIMIT and diff_last<FINISHED_LIMIT:
        return True
    else:
        diff_last=diff
        max_last=max_current
        return False
        
if __name__=='__main__':
    #初始化
    chromosome_states=init()
    n=100
    while n>0:
        n-=1
        fitnesses=fitness(chromosome_states)  #适应度计算
        if is_finished(fitnesses): #判断是否收敛
            break
        select_index=fiter(chromosome_states,fitnesses)#遴选，产生下一代
        chromosome_states=crossover(chromosome_states,select_index)
        chromosome_states=mutation(chromosome_states)
        print(chromosome_states)
        print(fitnesses)
print('最优个体：',BEST)
