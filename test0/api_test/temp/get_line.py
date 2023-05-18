# print([i for i in range(-5,5)])
n=int(input())
i=0
lines=[]
while i<n:
    i+=1
    s=input()
    lines.append([int(s.split(',')[0]),int(s.split(',')[1])])
    result=len(lines)
# print(lines)
class GLL:
    def get_point_set(self):
        point_set=[]
        for line in lines:
            point_set+=[p for p in range(int(line[0]),int(line[1]))]
        return point_set  #含重复点
        # return list(set(point_set))    #不含重复点
    def judge_line(self):
        for line in lines:
            line_point=[pt for pt in range(int(line[0]),int(line[1]))]



print(GLL().get_point())
