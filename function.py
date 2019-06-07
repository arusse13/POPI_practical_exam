def feature():
    return True
###Q1###
def number_of_above_averages(n,m,A):
    total=0
    for i in range(0,n):
        #print(i)
        for j in range(0,m):
           #print(A[i][j])
            total+=A[i][j]

    average=total/(n*m)
    #print(average)

    counter=0
    for i in range(0,n):
        for j in range(0,m):
            if A[i][j]>average:
                counter+=1
                #print(counter)

    return counter

#print(number_of_above_averages(2, 3, [[1,2,3],[4,5,6]]))

###Q2###
def common_elements(list1, list2):
    set1=set(list1)
    set2=set(list2)
    new_list = list(set1.intersection(set2))
    return new_list

###Q3###
class ManhattanTaxi:
    def __init__(self, initX, initY, consumption,init_fuel):
        self._cons=consumption
        self._pos=(initX, initY)
        self._fuel=init_fuel

    def moveto(self,X,Y):
        dist=abs(self._pos[0]-X)+abs(self._pos[1]-Y)
        if dist*self._cons < self._fuel:
            self._fuel -= dist*self._cons
            self._pos = (X, Y)
            return True
        else:
            return False

    def add_fuel(self,top_up):
        self._fuel+=top_up

###Q4###
def shortest_continuous_segment(s):
    occ_set=set(s)
    occ_list=[]

    for num in occ_set:
        occ_count = 0
        for i in range(0,len(s)):
            if s[i] == num and i != len(s)-1:
                occ_count += 1
            elif s[i] != num and occ_count!=0:
                occ_list.append((num, occ_count))
                occ_count=0
            elif s[i] == num and i == len(s)-1:
                occ_count += 1
                occ_list.append((num, occ_count))

    min_occur=occ_list[0][1]
    max_num=occ_list[0][0]

    for x in occ_list:
        if x[1]<min_occur:
            min_occur=x[1]
            max_num=x[0]

    for x in occ_list:
        if x[1] == min_occur and x[0]>max_num:
            max_num=x[0]

    result = (max_num,min_occur)

    return result

