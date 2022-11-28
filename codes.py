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
