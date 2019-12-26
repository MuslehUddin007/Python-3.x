def minion_game(string):
    con = ['A','E','I','O','U']
    length = len(string)
    sub = [string[i:j+1] for i in range(length) for j in range(i,length)]
    Stuart = list(set(filter(lambda x: x[0] not in con,sub)))
    Kevin = list(set(filter(lambda x: x[0] in con,sub)))
    SScore, KScore = 0,0
    for l in range(len(Stuart)):
        SScore += sum([1 for i in range(len(string)-len(Stuart[l])+1) if string[i:i+len(Stuart[l])] == Stuart[l]])
    for l in range(len(Kevin)):
        KScore += sum([1 for i in range(len(string)-len(Kevin[l])+1) if string[i:i+len(Kevin[l])] == Kevin[l]])

    return SScore,KScore

if __name__ == '__main__':
    s = input()
    SScore,KScore = minion_game(s)
    if SScore>KScore:
        print('Stuart %d'%(SScore))
    else:
        print('Kevin %d'%(KScore))