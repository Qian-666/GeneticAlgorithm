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
