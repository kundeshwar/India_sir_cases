import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu
import pandas as pd
import re 
#----------------------------------------page title

st.set_page_config(page_title="APRL", page_icon="🪴", initial_sidebar_state="expanded")
#------------------------------------------------sidebar written 
with st.sidebar:
    st.title('''      🍏 🍏 AIR POLLUTION        ''')
    st.markdown("------------------")
#st.title("Speciates India")
option_i = "🪔 Speciates India 🪔"
st.markdown(f"<h1 style='text-align: center;'>{option_i}</h1>",unsafe_allow_html=True) 
#----------------------------------------dictonary making 
# Dictionary to store the dataframes
file_dict = {}

# Pattern to extract the file name without the extension
pattern = r" -\s*(.+?)\.csv"
a = ['Speciates India -  B10EAF3C.csv','Speciates India -  B10WR3C.csv','Speciates India -  B25EAF3C.csv','Speciates India -  B25WR3C.csv','Speciates India -  C10WC3C.csv','Speciates India -  D10UPD1.csv','Speciates India -  K10CC3C.csv','Speciates India -  K10UPD2C.csv','Speciates India -  K10WC3C.csv','Speciates India -  M10WC3C.csv','Speciates India -  M25WC3C.csv','Speciates India -  P10UPD1.csv','Speciates India -  P25UPD1.csv','Speciates India - B10DG3C.csv','Speciates India - B10FC3C.csv','Speciates India - B10PD7C.csv','Speciates India - B10SD3C.csv','Speciates India - B10UPD1.csv','Speciates India - B25FC3C.csv','Speciates India - C10HSP3C.csv','Speciates India - C10PD7C.csv','Speciates India - C10SD4C.csv','Speciates India - C25HSP3C.csv','Speciates India - D10CP3C.csv','Speciates India - D10PD10C.csv','Speciates India - D10SD3C.csv','Speciates India - K10AW3C.csv','Speciates India - K10CP3C.csv','Speciates India - K10LS3C.csv','Speciates India - K10PD7C.csv','Speciates India - K10SD3C.csv','Speciates India - M10AP1.csv','Speciates India - M10FP3C.csv','Speciates India - M10FPD1.csv','Speciates India - M10GW3C.csv',
 'Speciates India - M10PB3C.csv','Speciates India - M10PD7C.csv','Speciates India - M10SD3C.csv','Speciates India - M25SD7C.csv','Speciates India - P10PD7C.csv','Speciates India - P10SD6C.csv','Speciates India - P25PD7C.csv']
file_2 = {}
for file_name in a:
    #print(file_name)
    match = re.search(pattern, file_name)
    #print(match)
    #file_2[match] = file_name
    if match:
        name = match.group(1)
        df = pd.read_csv(file_name)  # Read the CSV file as a dataframe
        file_dict[name] = df
        file_2[name] = file_name

#-------------------------------------------------see section 
option_a = "To View The Data"
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option_a}</h3>",unsafe_allow_html=True)
checked_v = st.sidebar.checkbox('Check me! to view')
if checked_v:
        selected_option_v = st.sidebar.selectbox('Select an ID', ('None', 'B10SD3C','C10SD4C','D10SD3C','K10SD2C','M10SD3C','P10SD6C','M25SD7C','P25SD6C',
        'B10PD7C','C10PD7C','D10PD10C','K10PD7C','M10PD7C','P10PD7C','P25PD7C','B10UPD1','D10UPD1','K10UPD2C','P10UPD1','P25UPD1','B10EAF3C','B25EAF3C','C10WC3C',
        'K10WC3C','M10WC3C','M25WC3C','B10WRC3C','B25WRC3C','K10CC3C','M10CC3C','M25CC3C','K10LW3C','B10FC3C','B25FC3C','K10LS3C','M10CON1','M10AP1',
        'K10AW3C','P10BC3C','K10BK3C','B10DG3C','C10SRM3C','C25SRM3C','M10GW3C','M10SW3C','M25SW3C','K10MW3CC','K10MW3C','M10KG3C','M25KG3C','M10LPG1','M10FPD1',
        'M10FP3C','M10PB3C','K10CP3C','D10CP3C','C10HSP3C','C25HSP3C'))
        if selected_option_v != "None":
               st.markdown("--------------------------")
               st.markdown(f"<h3 style='text-align: center;'>{selected_option_v}</h3>",unsafe_allow_html=True)
               st.dataframe(file_dict[selected_option_v])
#------------------------------------------function 
def add_data():
    
    st.success("Data successfully added!")


parameters = ['Id', 'Name', 'Specie', 'Mass', 'Uncertainity', 'Analythical Method',
                  'Uncertainty Method', 'Particle Size', 'N Samples', 'Reference',
                  'Country', 'Place', 'Test Year', 'Sampling Method', 'Latitude',
                  'Longitude', 'CAS Number', 'Symbol', 'Reference.1', 'Link',
                  'Other comments']
 
def text(parameters):
    #---------------------------0
    d_0 = st.text_input("ID")
    data[parameters[0]] = d_0
    if d_0 == "":
        st.error("Required filled")
    #----------------------------1
    d_1 = st.text_input("Name")
    data[parameters[1]] = d_1
    if d_1 == "":
        st.error("Required filled")
    #-----------------------------2
    d_2 = st.text_input(parameters[2])
    data[parameters[2]] = d_2
    if d_2 == "":
        st.error("Required filled")
    #------------------------------3
    d_3 = st.number_input(parameters[3])
    data[parameters[3]] = d_3
    if d_3 == "":
        st.error("Required filled")
    #----------------------------4
    d_4 = st.number_input(parameters[4])
    data[parameters[4]] = d_4
    if d_4 == "":
        st.error("Required filled")
    #----------------------------5
    d_5 = st.text_input(parameters[5])
    data[parameters[5]] = d_5
    if d_5 == "":
        st.error("Required filled")
    #----------------------------6
    d_6 = st.text_input(parameters[6])
    data[parameters[6]] = d_6
    if d_6 == "":
        st.error("Required filled")
    #-----------------------------7
    d_7 = st.text_input(parameters[7])
    data[parameters[7]] = d_7
    if d_7 == "":
        st.error("Required filled")
    #-----------------------------8
    d_8 = st.number_input(parameters[8])
    data[parameters[8]] = d_8
    if d_8== "":
        st.error("Required filled")
    #-----------------------------9
    d_9 = st.text_input(parameters[9])
    data[parameters[9]] = d_9
    if d_9 == "":
        st.error("Required filled")
    #------------------------------10
    d = st.text_input(parameters[10])
    data[parameters[10]] = d
    if d == "":
        st.error("Required filled")
    #------------------------------11
    d = st.text_input(parameters[11])
    data[parameters[11]] = d
    if d == "":
        st.error("Required filled")
    #-----------------------------12
    d = st.text_input(parameters[12])
    data[parameters[12]] = d
    if d == "":
        st.error("Required filled")
    #----------------------------13
    d = st.text_input(parameters[13])
    data[parameters[13]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------14
    d = st.number_input(parameters[14])
    data[parameters[14]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------15
    d = st.number_input(parameters[15])
    data[parameters[15]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------16
    d = st.text_input(parameters[16])
    data[parameters[16]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------17
    d = st.text_input(parameters[17])
    data[parameters[17]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------18
    d = st.text_input(parameters[18])
    data[parameters[18]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------19
    d = st.text_input(parameters[19])
    data[parameters[19]] = d
    if d == "":
        st.error("Required filled")
    #---------------------------20
    d = st.text_input(parameters[20])
    data[parameters[20]] = d
    if d == "":
        st.error("Required filled")
def csv_save(ma, df):
    for i in a:
        match = re.search(pattern, i)
        if match == ma:
            df.to_csv(i, index=False)

#------------------------------------------------------add section           
st.sidebar.markdown("------------------")
option_a = "To Add The Data"
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option_a}</h3>",unsafe_allow_html=True)
checked_a = st.sidebar.checkbox('Check me! to add')
if checked_a:
        st.sidebar.write("Please fill both & Enter")
        selected_option_a = st.sidebar.selectbox('Select ID', ('None', 'B10SD3C','C10SD4C','D10SD3C','K10SD2C','M10SD3C','P10SD6C','M25SD7C','P25SD6C',
        'B10PD7C','C10PD7C','D10PD10C','K10PD7C','M10PD7C','P10PD7C','P25PD7C','B10UPD1','D10UPD1','K10UPD2C','P10UPD1','P25UPD1','B10EAF3C','B25EAF3C','C10WC3C',
        'K10WC3C','M10WC3C','M25WC3C','B10WRC3C','B25WRC3C','K10CC3C','M10CC3C','M25CC3C','K10LW3C','B10FC3C','B25FC3C','K10LS3C','M10CON1','M10AP1',
        'K10AW3C','P10BC3C','K10BK3C','B10DG3C','C10SRM3C','C25SRM3C','M10GW3C','M10SW3C','M25SW3C','K10MW3CC','K10MW3C','M10KG3C','M25KG3C','M10LPG1','M10FPD1',
        'M10FP3C','M10PB3C','K10CP3C','D10CP3C','C10HSP3C','C25HSP3C'))
        password= st.sidebar.text_input("Password")
        if selected_option_a != "None" and password=="Kundeshwar20@":
            data = {}
            text(parameters)
            c = st.button("Add into data")
            if c:
                add_data()
                # Create a new dataframe from the new row
                new_row_df = pd.DataFrame([data])

                # Concatenate the original dataframe with the new row dataframe
                df = pd.concat([file_dict[selected_option_a], new_row_df], ignore_index=True)
                # Fix the column types if necessary
                df['Test Year'] = pd.to_numeric(df['Test Year'], errors='coerce')
                file_dict[selected_option_a] = df
                print(file_2)
                i = file_2[selected_option_a]
                df.to_csv(i, index=False)
                # Fix the column types if necessary
                csv_save(selected_option_a, df)
                #print(data)
                data = {}
                st.markdown("--------------------------")
                st.markdown(f"<h3 style='text-align: center;'>{selected_option_a}</h3>",unsafe_allow_html=True)
                st.dataframe(file_dict[selected_option_a])
                st.write("Go the upward and clear first response and add another one")
        else:
            st.markdown("--------------------")
            st.markdown("""
            - Send an email to kundeshwar15000@gmail.com requesting the password.
            - In the email, provide your username and any additional information required to verify your account.
            - Our support team will review your request and respond to your email within 24 hours.
            - Once your request is approved, you will receive an email with the password for accessing your account.
            - Use the provided password to log in to the web app.""")
#-------------------------------------------------------bottom of sidebar 
st.sidebar.markdown("------------------")
option= "&#8595;"
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
option = "  "
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
option = "  "
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
option = "  "
st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)

st.sidebar.write('Made with ❤️ by IIT Bombay 😍')









