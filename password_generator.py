import streamlit as sl
import random
sl.title('Rattle password generator')
inp=sl.number_input('Enter the length of your password:',min_value=1)
if sl.button('Generate!'):
    a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    r=random.sample(a,inp)
    a="".join(r)
    sl.header(a)