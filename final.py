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

print(l_str)
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
