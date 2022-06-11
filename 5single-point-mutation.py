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

