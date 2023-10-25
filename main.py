import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split



# this file is open csv formet 
# df = pd.read_csv('data.csv')
# st.write(df)
# st.dataframe(df, height=300, width=800)

# this file is open json formet
# a = {
#     'name': ['abs', 'xyx'],
#     'marks': [87, 95]
# }
# df = pd.read_csv('data.csv')
# st.title('Data Analytics')
# st.write(a) # this write formet
# st.table(a) # this table formet 





# Data Mining
df = pd.read_csv('data.csv')
st.title("Data Analytics")
col1, col2, col3 = st.columns(3)
col1.metric("Name", 'a', 'b')
col2.metric("Marks", 82,87)

# df1 = df.drop(['ID', 'Year', 'Category', 'Product', 'UnitPrice', 'TotalPrice'], axis='columns')
# st.write(df1)




# load dataset 
if st.sidebar.button("load dataset"):
 st.write(df)

# load discription
if st.sidebar.button("load discription"):
    st.write(df.describe())

if st.sidebar.button("load bar chart "):
  df2 = df.head(20)
  fig = plt.figure(figsize=(10,8))
  plt.bar(df2['Product'], df2['Qty'])
  st.pyplot(fig)

# side bar 
st.sidebar.button("Hello")



















# st.map(data=df1,  latitude='Country', longitude='Qty',
#         color=None, size=500, zoom=50, use_container_width=True)
