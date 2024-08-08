import streamlit as st
import sqlite3
import pandas as pd
st.write(sqlite3.sqlite_version)

conn = sqlite3.connect('example.db')
c = conn.cursor()

def view_db():
    c.execute("SELECT * FROM people")
    return c.fetchall()

st.title("SQL EXAMPLE IN STREAMLIT")

samples = view_db()
st.write(samples[0])
print(samples)
#samples [(1, 'Alice', 30), (2, 'Bob', 25)]
#samples[0] (1, 'Alice', 30)
#samples[0][1] 'Alice'
st.metric(label=samples[0][1], value=samples[0][2], delta=samples[0][2]-samples[1][2])#, delta="1.2 °F")

df = pd.DataFrame(samples, columns=['ID','name','age'])
st.dataframe(df)


#col1, col2, col3 = st.columns(3)
#col1.metric("Temperature", "70 °F", "1.2 °F")
#col2.metric("Wind", "9 mph", "-8%")
#col3.metric("Humidity", "86%", "4%")