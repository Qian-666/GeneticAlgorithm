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
