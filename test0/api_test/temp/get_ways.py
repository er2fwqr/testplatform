# def get_ways(n:int):
#     w=[i for  i in range(0,n+1)]
#     w[0]=0
#     w[1]=1
#     for n in range(2,n+1):
#         w[n]=w[n-1]+w[n-2]
#     return w[n]
# print(get_ways(50))
def count_ways(n):
    if n <= 1:
        return 1

    # 创建一个列表来保存每一步的方法数
    ways = [0] * (n + 1)
    print(ways)
    # 初始条件
    ways[0] = 1
    ways[1] = 1

    # 通过迭代计算每一步的方法数
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    print(ways)
    return ways[n]

# 测试
n = 50
total_ways = count_ways(n)
print("总共有", total_ways, "种方法")
