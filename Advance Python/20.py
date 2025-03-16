a=[10,'hai',3+4j,'hello',9.8]
print([len(i) if type(i) in [str,list,tuple,set,dict] else 1 for i in a])