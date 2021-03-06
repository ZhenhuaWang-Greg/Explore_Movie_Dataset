#!/usr/bin/env python
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().run_line_magic('matplotlib', 'inline')

movie_data = pd.read_csv('./tmdb-movies.csv')


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[2]:


display(movie_data.tail())
display(movie_data.sample()) #random row from the movie_data with title
display(movie_data.dtypes)
display(movie_data.isnull().any(axis = 0))
display(movie_data.isnull().sum())
display(movie_data.describe())
display(movie_data.head())


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[3]:


'''clean data: 
movie_data_fill fills nan with 0, and movie_data_drop drops the rows with nan'''
movie_data_fill = movie_data.fillna(0)
movie_data_drop = movie_data.dropna(axis = 1)


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[4]:


#1st: set a new form with columns of id, popularity, budget, runtime and vote_average
display(movie_data_fill[['id', 'popularity', 'budget', 'runtime', 'vote_average']])
#3rd: set a new form woth rows from 50 to 60 and columns of popularity
display(movie_data_fill.iloc[list(range(49,60)), 2])
#2nd
display(movie_data_fill.iloc[list(range(20))+[47,48], :])


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[5]:


#movies of which the popularity is larger than 5
display(movie_data_fill[movie_data_fill['popularity'] > 5])
#movies of which the popularity is larger than 5 and the release year is later than 1996
display(movie_data_fill[(movie_data_fill['popularity'] > 5) & (movie_data_fill['release_year'] >= 1996)])


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[6]:


#data groupped by release year and the values are the mean of that year's revenue
movie_group_by_revenue_mean = movie_data_fill.groupby(['release_year']).revenue.agg('mean')
#data groupped by director and in the descending order of the average popularity of the movies which he/she directed
moive_group_by_popularity_mean_descending = movie_data_fill.groupby(['director']).popularity.agg('mean').sort_values(ascending = False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[27]:


movie_popularity = movie_data.sort_values(by = 'popularity', ascending = False)
movie_name = movie_popularity.loc[:, 'original_title'].values[:20]#only need the first 20 names
movie_popularity_number = movie_popularity.loc[:, 'popularity'].values[:20]#only need the the first 20 numbers
plt.bar(movie_name, movie_popularity_number, color = sb.color_palette()[0])#use bar chart
plt.xticks(rotation = 90)
plt.xlabel('moive names')
plt.ylabel('popularity')


# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[16]:


#profit caculation and insertion, succeeded
movie_data.insert(20, column = 'profit', value = (movie_data.loc[:, 'revenue_adj'].values - movie_data.loc[:, 'budget_adj'].values)/ (1e+09))
plt.figure(figsize = [10, 5])
#boxplot failed
#sb.boxplot(data = movie_data, x = 'profit', y = 'release_year', color = sb.color_palette()[0])
#plt.xticks(rotation = 90)
#plt.xlim(-0.1, 0.2)
#errorbar
plt.subplot(1, 2, 1)
x = np.unique(movie_data['release_year'].values)
y_median = movie_data.groupby('release_year').profit.median()
y_q1 = movie_data.groupby('release_year').profit.quantile(0.25)
y_q3 = movie_data.groupby('release_year').profit.quantile(0.75)
base_color = sb.color_palette()[0]
line_color_median = sb.color_palette()[1]
line_color_q1 = sb.color_palette()[2]
line_color_q3 = sb.color_palette()[3]
plt.scatter(data = movie_data, x = movie_data['release_year'], y = movie_data['profit'], alpha = 0.1)
plt.errorbar(x, y = y_median, c = line_color_median)
plt.errorbar(x, y = y_q1, c = line_color_q1, linestyle = '--')
plt.errorbar(x, y = y_q3, c = line_color_q3, linestyle = '--')
plt.ylim(-0.05, 0.05)
plt.xlabel('year')
plt.ylabel('median, q1 and q3')
#bar of means
plt.subplot(1, 2, 2)
x = np.unique(movie_data['release_year'].values)
y_means = movie_data.groupby('release_year').profit.mean()
plt.bar(x, y_means, color = base_color)
plt.xlabel('year')
plt.ylabel('mean')
'''利润的中位数基本保持平稳，尽在1980-2000年间出现较大波动，1/4位数呈现下降趋势，高利润的影片数量在减少。
虽然3/4位数也较为平稳，但是从散点图可以看出更多的影片集中在亏损。总体来说影片的盈利能力较早年分化更严重。
平均盈利能力逐年下降，近年逐渐趋平。'''


# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# In[ ]:





# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# In[ ]:





# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# In[ ]:





# > 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。
