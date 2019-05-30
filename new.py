from word2number import w2n

#numbers={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'million':None,'billion':None,'trillion':None,'point':None,'dot':None,'o':None}
text = 'my one credit card number is one thousand one two three four five three two one four eight nine zero thirty four five'
l_text = text.split(' ')
ref = l_text.copy()
#tys=('twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')

to_be_rem=[]
for i in l_text:
    try:
        print(i)
        result=w2n.word_to_num(i)
        print(result,'this is result')
        l_text[l_text.index(i)]='X'
    except Exception as e:
        print(e)
        continue
print(text)
print(l_text)
print(' '.join([str(i) for i in l_text]))
