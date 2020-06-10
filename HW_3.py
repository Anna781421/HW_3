#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Я не знаю откуда были взяты данные для построения графиков из примера, поэтому для построения своих я воспользуюсь одним из датасетов. 

# In[ ]:


wine = pd.read_csv("wine.csv")


# Для построения графиков, введем дополнительные параметры: итог ('sum') и округленный pH ('pH1'). Итогом будет классификация основанная на качестве ('quality'), где 2 - отличное вино, 1 – хорошее, а 0 – удовлетворительное. 

# In[115]:


wine['sum'] = wine['quality'].apply(lambda value: '0' if value < 5 else '1' if value < 6 else '2')
wine['pH1'] = wine['pH'].apply(lambda value: 3 if value < 3.5 else 4)


# # Построение графиков идентичных примеру. 

# In[121]:


fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8, 3))
sns.despine(right=True)
sns.set_style('white')
sns.set_palette('hot')
g1 = sns.barplot(x="pH1",y="citric acid", data=wine, ax=ax2)
g2 = sns.lineplot(x="sum", y="alcohol", hue='pH1', err_style="bars", data=wine, ax=ax1, legend='full')
ax1.set_title('График.1.')
ax2.set_title('График.2.')
ax1.tick_params(left=True, bottom=True)
ax2.tick_params(left=True, bottom=True)
ax1.legend(frameon=False, loc='upper center')
fig.suptitle('Графики о вине')
plt.show()


# График 1 иллюстрирует зависимость содержания алкоголя ('alcohol') от итога ('sum').
# График 2 показывает усредненное содержание лимонной кислоты ('citric acid') в зависисмости от итога ('sum').
