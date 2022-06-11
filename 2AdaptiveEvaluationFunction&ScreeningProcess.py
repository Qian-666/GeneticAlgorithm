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
