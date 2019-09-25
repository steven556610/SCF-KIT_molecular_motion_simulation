
# coding: utf-8

# In[1]:


#進行數據分析之前常要引用的函式庫
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import csv
import matplotlib.pyplot as plt


# In[2]:


#產生100筆資料，每筆資料都是2個數字
csvfile=open(r'E:\domin3的平面投影點與軸的距離寫入_new.csv','r')
csvread = csv.reader(csvfile)
x = list(csvread)
x = np.array(x)
print(x)


# In[3]:


#第一筆長這樣
x[0]


# In[ ]:


#畫出來看看，想當然是平均的佈滿整個畫面
#然後我們會用KMeans硬把他分類(明明沒意義的100個點……但他就是分的出來)
plt.scatter(x[:,0],x[:,1],s=50)


# In[4]:


#接下來匯入KMeans函式庫
from sklearn.cluster import KMeans


# In[5]:


#請KMeans分成三類
clf = KMeans(n_clusters=2)


# In[6]:


#開始訓練！
clf.fit(x)


# In[7]:


#這樣就可以取得預測結果了！
clf.labels_


# In[9]:


output = open(r'E:\K-mean.csv','w')
for line in clf.labels_:
    output.write(str(line)+'\n')
output.close()


# In[ ]:


#最後畫出來看看
#真的分成三類！太神奇了………無意義的資料也能分～
plt.scatter(x[:,0],x[:,1], c=clf.labels_)
#KMeans的使用時機就在於～你根本不知道測試的資料有什麼特性的時候
#就是用他的時候了，我稱KMeans為盲劍客 XD

