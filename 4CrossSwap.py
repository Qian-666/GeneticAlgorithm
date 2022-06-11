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

