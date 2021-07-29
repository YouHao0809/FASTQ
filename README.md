# FASTQ
## 序列数据分析

**1.**  **背景知识**

FASTQ格式是一种常用的序列文件格式，是当前高通量测序数据的标准格式。illumina测序得到的原始图像数据经过Base Calling转化为序列数据，结果以FASTQ文件格式来存储，包含测序read的序列信息以及测序质量信息。

FASTQ文件格式如下所示：

```python
@K00169:186:HM5C2CCXX:6:1101:8136:2962 1:N:0:CTGGCATA

CCACTCATAATCCAGCAAATACTAAATCTGCTGCAGGAAAAGAAATGCGGTTGAGCTT

+

AFFKKFKKFFKKKKFKAFKKAAKFAFFKKFKKFFKKKKFKAFKKAAKFAFFKKFKKFFKF
```

第一行：区分不同reads的ID号。以’@’开始，后面跟着序列的描述信息。

第二行：序列信息，由碱基以及N组成。

第三行：'+'，或者与第一行相同，无特殊意义。

第四行：第二行序列中每个碱基对应的测序质量值，以ASCII码表示。

 

近年来，测序质量多采用Phred33编码方式，碱基质量得分Q与ASCII值的关系是：ASCII值 = Q + 33。一般，碱基质量为0 ~ 40，即ASCII值范围为33 ~ 73，对应字符为！~ I 。

根据碱基质量得分可以评估测序出错率，碱基质量得分Q与测序错误率P的换算关系为：**Q = -10log10P** **。**

对于测序得到的FASTQ文件，通常需要进行常规的序列分析，来评估测序质量。比如，测序得到的reads数量、碱基含量分布（包括错误碱基N的含量分布）、GC含量分布、碱基质量分布等统计。

 

**2.**  **实验目的**

熟练使用python语言，对序列数据进行分析和可视化。

**3.**  **实验任务**

给定FASTQ文件“data1.fq”，进行如下分析。

1）GC含量统计并作图显示。计算每条read中的GC含量（即G+C的总含量），并用直方图显示。

 

2）统计所有reads在各位置上ACGT碱基以及N的含量分布，并作图显示。

 

3）将FASTQ文件中测序质量序列转换为碱基质量，统计所有reads在各位置上碱基质量分布，并作图显示。

 

4）产生低质量FASTQ文件“data1_low.fq”。对于给定的文件“data1.fq”，随机选择给定比例p（比如p=0.05）的reads，并对选择的reads随机选择k（k < len(read), 比如k = 15）个位置，将这k个位置上的碱基替换为字符“N”。用参数“-p 0.05 –k 15”运行脚本，得到低质量FASTQ文件“data1_low.fq”；然后，用题2）中的脚本重新统计各位置上的ACGT碱基以及N的含量分布，看是否有变化。

 

5）去除低质量FASTQ文件“data1_low.fq”中质量较低的read条目，生成高质量FASTQ文件“data1_high.fq”。考虑reads中N的数量以及reads中碱基的质量，当read中N的数量大于n或者reads中低质量碱基比例超过r（将质量低于q的碱基视为低质量碱基），则去除该read条目。用参数“-n 10 –q 20 –r 0.1”运行脚本，得到处理后的FASTQ文件“data1_high.fq”；然后，用题2）中的脚本重新统计各位置上的ACGT碱基以及N的含量分布，看是否有变化。

 

**4.**  **实验报告要求**

将实验任务的题目、以及对应的代码及图表结果等信息编辑在一个.doc文件中（注意代码缩进，代码用五号字号，其他文字用小四字号）。

 