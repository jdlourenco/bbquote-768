import streamlit as st
from bbquote.lib import get_quote

"dgfdg"

1

if st.button("Get a bbquote"):
    quote = get_quote()
    st.text(quote)
