# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pkcVBpleliM-xvs1klESlhN02c6CFosQ
"""


# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

import streamlit as st
x=st.number_input("enter the first number")
y=st.number_input("enter the second number")
z=st.number_input("enter the third number")
if((x>=y) & (x>=z)):
    st.write (largest among three numbers is x)
elif((y>=x) & (y>=z)):
    st.write (largest among three numbers is y)
else:
    st.write (largest among three numbers is z)

