import os
from matplotlib import pyplot as plt

# 处理四行数据返回字典
def process(lines=None):
    ks = ['name', 'sequence', 'optional', 'quality']
    return {k: v for k, v in zip(ks, lines)}


# 检查数据文件路径
try:
    fn = "./data1.fq"
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

# 加载数据
records = []
n = 4
with open(fn, 'r') as fh:
    lines = []
    for line in fh:
        lines.append(line.rstrip())
        if len(lines) == n:
            record = process(lines)
            records.append(record)
            # print (record)
            lines = []
print(records[1])

# 第一问
q1 = []
for record in records:
    sum_GC = 0
    for index, value in enumerate(record['sequence']):
        if (value == 'G' or value == 'C'):
            sum_GC += 1
    q1.append(sum_GC)


# 参数依次为list,抬头,X轴标签,Y轴标签,XY轴的范围
def draw_hist(myList, Title, Xlabel, Ylabel, Xmin, Xmax, Ymin, Ymax):
    plt.hist(myList, bins=200, color=['slateblue'], edgecolor=[
             0.8, 0.8, 0.8, 0.8], alpha=0.5)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin, Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin, Ymax)
    plt.title(Title)
    plt.show()


draw_hist(q1, 'GC', 'Quality', 'Number', 0, 150, 0, 300)

# 第二问
# 绘图函数
def draw_linechart(query_records):

    # 求出数据总条数
    length = len(query_records)

    count_A = [0]*150
    count_G = [0]*150
    count_C = [0]*150
    count_T = [0]*150
    count_N = [0]*150

    for record in query_records:
        for index, single_char in enumerate(record['sequence']):
            if (single_char == 'A'):
                count_A[index] += 1
            if (single_char == 'G'):
                count_G[index] += 1
            if (single_char == 'C'):
                count_C[index] += 1
            if (single_char == 'T'):
                count_T[index] += 1
            if (single_char == 'N'):
                count_N[index] += 1

    new_count_A = [i/length for i in count_A]
    new_count_G = [i/length for i in count_G]
    new_count_C = [i/length for i in count_C]
    new_count_T = [i/length for i in count_T]
    new_count_N = [i/length for i in count_N]

    plt.plot(new_count_A, 'crimson', label='A')
    plt.plot(new_count_G, 'palegreen', label='G')
    plt.plot(new_count_C, 'gold', label='C')
    plt.plot(new_count_T, 'lightskyblue', label='T')
    plt.plot(new_count_N, 'coral', label='N')

    plt.title('AGCTN distribution')
    plt.xlabel('location')
    plt.ylabel('percentage')
    plt.legend()
    plt.show()


draw_linechart(records)


# 第五问
n = 10
q = 20
r = 0.1
sum_N = 0
new_records = []
for record in records:
    for single_char in record['sequence']:
        if single_char == 'N':
            sum_N += 1

    if sum_N < n:
        sum_low = 0
        for single_char in record['quality']:
            if (ord(single_char)-33) < q:
                sum_low += 1
        if (sum_low/150 < r):
            new_records.append(record)

# 绘图
draw_linechart(new_records)
