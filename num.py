from word2number import w2n
text = 'my one credit card number is nine six zero one five three nine nine six one zero six six seven eight two zero one two three four five three two one four eight nine zero thirty four five'

l_str = text.split(' ')

for i in range(len(l_str)):
    print(i)
    #is_cc(index=i,data=l_str[i:i+15])
    for every_part in l_str[i:i+15]:
        try:
            result=w2n.word_to_num(every_part)
            if w2n.word_to_num(every_part) in (0,1,2,3,4,5,6,7,8,9,0,10,20,30,40,50,60,70,80,90,100,1000,10000,100000):
                print('found')
                l_str[l_str.index(every_part)]=str(result)
        except Exception as e:
            print(e)
            continue

print(' '.join(l_str))

