from multiprocessing import Pool
def sq(n):
    return n*n
if __name__=='__main__':
    array=[1,2,3,4,5,6,7,8,9]
    p=Pool(processes=4)
    result=p.map(sq,array)
    for n in result:
        print(n)
