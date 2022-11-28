# Flatten-Func
The code that Flatted a list

#SORU 1 Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
output: [1,'a','cat',2,3,'dog',4,5]


```
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_List = []

def flatten(l):
    for _ in l:
        if type(_) == list:
            flatten(_)
        else:
            flatten_List.append(_)
    return flatten_List
print(flatten(l))
```
