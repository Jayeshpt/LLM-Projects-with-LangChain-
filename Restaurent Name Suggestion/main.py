import streamlit as st 
import langchainfile



st.title('Restaurent Name Generator')

cuisine = st.sidebar.selectbox("pick a cuisine",('Indian','Italian','Chinese','Japanese','French','Thai','Greek','Brazilian','Moroccan','Spanish','Lebanese','Turkish','Vietnamese','Korean','Ethiopian','Jamaican','Russian','Peruvian',
'Malaysian','Egyptian','Swedish'))



if cuisine:
    respose = langchainfile.generate_restaurant_name_and_items(cuisine)

    st.header(respose['restaurant_name'].strip())

    menu_items = respose['menu_items'].strip( ).split(",")
    st.write("***Menu Items***")
    for item in menu_items:
        st.write(item)


    