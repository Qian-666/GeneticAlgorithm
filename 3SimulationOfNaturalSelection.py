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
