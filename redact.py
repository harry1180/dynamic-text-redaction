
from word2number import w2n
text = 'my one credit card number is nine six zero one five three nine nine six one zero six six seven eight two zero one two three four five three two one four eight nine zero thirty four five'

l_str = text.split(' ')

#e for e in l_str if e, l_str[l_str.index(e)+1
#credit card check
'''def is_cc(index=0,data=l_str[index:index+15]):
    print('iteration started')
    print(l_str[i:i+15])
    for every_part in l_str[i:i+15]:
        try:
            result=w2n.word_to_num(every_part)
            if w2n.word_to_num(every_part) in (0,1,2,3,4,5,6,7,8,9,0,10,20,30,40,50,60,70,80,90,100,1000,10000,100000):
                print('found')
                l_str[l_str.index(every_part)]=str(result)
            #cc = (int(i) for i in data)
            #print(cc)
            if sum((int(j) for j in l_str[i:i+15])):
            #if sum((1,2,3,4)):
                    print('credit card found')
                    l_str[i:i+11]='XXXX-XXXX-XXXX-'



        except Exception as e:
            print(e)
            continue
'''
for i in range(len(l_str)):
    print(i)
    #is_cc(index=i,data=l_str[i:i+15])
    for every_part in l_str[i:i+15]:
        try:
            result=w2n.word_to_num(every_part)
            if w2n.word_to_num(every_part) in (0,1,2,3,4,5,6,7,8,9,0,10,20,30,40,50,60,70,80,90,100,1000,10000,100000):
                print('found')
                l_str[l_str.index(every_part)]=str(result)
            #cc = (int(i) for i in data)
            #print(cc)
            '''if sum((int(j) for j in l_str[i:i+15])) and i+15 < (len(l_str)-4):
            #if sum((1,2,3,4)):
                    print('credit card found')
                    print(l_str[i:i+15])
                    l_str[i:i+11]='XXXXXXXXXXX'
                    print(l_str[i:i+15],'hey')'''



        except Exception as e:
            print(e)
            continue
print(l_str)
'''for l in range(len(l_str[:15])):
    for each in l_str[:-4]:
        #while l_str.index(each)+9  
        try:
            if each.isdigit() and l_str[l_str.index(each)+1].isdigit() and  l_str[l_str.index(each)+2].isdigit() and  l_str[l_str.index(each)+3].isdigit() and l_str[l_str.index(each)+4].isdigit() and l_str[l_str.index(each)+5].isdigit() and l_str[l_str.index(each)+6].isdigit() and l_str[l_str.index(each)+7].isdigit():
                l_str[l_str.index(each)],l_str[l_str.index(each)+1],l_str[l_str.index(each)+2],l_str[l_str.index(each)+3],l_str[l_str.index(each)+4],l_str[l_str.index(each)+5],l_str[l_str.index(each)+6],l_str[l_str.index(each)+7],l_str[l_str.index(each)+8],l_str[l_str.index(each)+9]='X','X','X','X','X','X','X','X','X','X'
                print('end')
        except Exception as e:
            print(e)
            continue
print(' '.join(l_str))
print(text)'''
import re

PATTERN = "([4-6]{1})([0-9]{3}-?)([0-9]{4}-?){2}([0-9]{4})"

h1=' '.join(l_str)
def is_valid_creditcard(sequence):
    """Check if a sequence is a valid credit card number.
    Rules for sequences to qualify as credit card numbers:

    Sequences must:

    -Contain exactly 16 digits;
    -Start with a 4,5 or 6;
    -Only consist of digits (0-9).

    Sequences may:
    -Have digits in groups of 4, separated by one hyphen.

    Sequence must not:
    -Use any other separator;
    -Have 4 or more consecutive repeated digits.
    """
    for i, n in enumerate(sequence):
        try:
            if (sequence[i], 
                sequence[i+1], 
                sequence[i+2],
                sequence[i+3],
                sequence[i+4],
                sequence[i+5],
                sequence[i+6],
                sequence[i+7]
            ) == (n,'', n, '', n,'',  n,''):
                return False
        except IndexError:
            pass
    return bool(re.match(PATTERN, sequence))
#h1=h1.replace(' ','')
print(h1)
h2=' '.join(l_str)
for i in range(len(h1)):
    #for e in h1[i:i+15]:
    if i+32 ==len(h1):
        break
    print(h1[i:i+32])
    res=is_valid_creditcard(h1[i:i+32].replace(' ',''))
    if res:
        #print(' '.join(h1),'hurray')
        h1=h1[:i]+'X X X X X X X X X X X X '+h1[i+24:]

        #h1[i:i+12]='XXXXXXXXXXXX'

print(is_valid_creditcard('6015399610667820'))
print(h1)
print(text)
