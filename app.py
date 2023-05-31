import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
              st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("css/style.css")

hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_wpaclr3s.json")
pro1 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_RzSHYh.json")
pro2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rqwsqnj.json")
pro3 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qpsnmykx.json")
lottie_coder = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ctqgzmyh.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_HxqVQ4.json")
cirt = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json")
cirt2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_2znxgjyt.json")
cirt3 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_dqazhefa.json")
cirt4 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_sqwEc44qxw.json")
image = Image.open("IMG_0001.JPG")

co1, co2 = st.columns((1,2))
with co1:
    st.title("Welcome to my Portfolio") 
    st.image(image, width = 200)
with co2:
    st_lottie(hello, height=300)
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Certifications','Contact','Blogs'],
        icons = ['person','code-slash','award','chat-left-text-fill','browser-chrome'],
        orientation = 'horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.title("I am Raj Kumar Gubbala")
            st.subheader("Graduated from KITS Engineering Collage" )
        with col2:
            st_lottie(lottie_coder)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            :book: EDUCATION
                 """)
            st.write("""
            - KITS Engineering Collage (2018 - 2022)
                 - Bachelor of Technology : Computer Science and Engineering
                 - Percentage : 64%
            - Sri Chaitanya JR Collage (2016 - 2018)
                 - Intermediate : MPC
                 - Precentage : 68%
            - J. Sikile School         (2004 - 2016)
                 - 10th
                 - Percentage : 74%
                 """)

        with col4:
            st.subheader("""
            :computer: SKILLS
            - Python
            - SQL
            - Data Analysis
            - Data Visuilization
            - PowerBI
            - Tableau
            - MS Excel
            - Web Scraping
            - Statistics
            - Machine Learning
            """)

    st.write("---")

    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            st.subheader("""
            :male-student: PERSONAL COMPETENCIES
            - Communication Skills
            - Presentation Skills
            - Work Ethic
            - Quick Learner 
            - Problem Solving
            - Teamwork Skills
            - Positive Attitude
            - Self Confidence
            """)

        with col6:
            st.subheader("""
            :man-bouncing-ball: HOBBIES/INTERESTS
            - Playing Football
            - Solving Puzzles
            - Travelling
            - Learning New Technologies
            - Learning new things
            """)

    st.write("---")

    with st.container():
        co, lo = st.columns(2)
        with co:
            st.subheader("""
            :microphone: LANGUAGES
            - English
            - Telugu
            - Hindi
            """)

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col7, col8 = st.columns((1,2))
        with col7:
            st.subheader("1)")
            st_lottie(pro1)
        with col8:
            st.subheader("HAND WEB BROWSER")
            st.subheader("""
            Objective of the Project:- 
            - The Objective of my hack is to design a robust and efficient system which will be able to control the browser via hand gestures i.e. different hand gestures will be assigned to different sites. So, if we show a particular hand gesture, a particular site will open up in a new tab.
            -  I plan to design a system to solve above problem using image processing techniques and controlling the browser using hand gestures. At, first the user needs to enter the sites which he/she frequently visits and needs to control those sites using hand gestures. A user needs to enter the site names for the particular hand gestures. That’s all, the user can now control the browser, open sites in new tabs using hand gesture and can even close the browser using the hand gesture. Thus, a hand gesture controlled browser is made.
               In this way a user can easily open the sites which he/she wants in the new tab using the hand gesture.
            """)
            
            st.markdown("[Visit Github Repo](https://github.com/Rajkumargubbala/Hand_Web_Browser)")
    st.write("---")
    with st.container():
        col9, col10 = st.columns((1,2))
        with col9:
            st.subheader("2)")
            st_lottie(pro2)
        with col10:
            st.subheader("EXPLORATORY DATA ANALYSIS ON USED BIKE PRICES")
            st.subheader("""
            Problem Statement:-
            - Find which type of used bikes are available in cities and what are the different price ranges of the bikes
            """)
            st.subheader("""
            Objective of the Project:-
            - Finding a desired Used Bikes in the affordable price with respect to City
            - To visualize the data using various visualization techniques
            """)
            st.subheader("""
            Summary:-
            - I have selected  Bike wale website for our web scraping project
            - Request to the website
            - Import Beautiful Soup and all the necessary libraries for scraping data
            - Check length’s of all columns  and create the DataFrame 
            - Export into .csv format and read csv file  and  clean the Data
            - Analysis of Univariate, Bivariate and Multivariate
            """)
            st.markdown("[Visit Github Repo](https://github.com/Rajkumargubbala/Exploratory-Data-Analysis)")
            
    st.write("---")
    with st.container():
        col11, col12 = st.columns((1,2))
        with col11:
            st.subheader("3)")
            st_lottie(pro3)
        with col12:
            st.subheader("SQL PROJECT:-  MUSIC STORE DATA ANALYSIS")
            st.subheader(""" 
            Description:-
            - I have created all the required tables with the required constraints which will help to create the relationship between the tables.
            - Derived the required constraints to make use of the schema diagram of the project. 
            """)
            st.subheader("""
            Objective of the Project:-
            - Finding and Analyzing the Music Store Data using SQL Querries.
            """)
            st.markdown("[Visit Githuib Repo](https://github.com/Rajkumargubbala/SQL-PROJECT--MUSIC-STORE-DATA-ANALYSIS)")

    st.write("---")

if selected == "Certifications":
    with st.container():
        st.header("My Cretifications")
        st.write("##")
        cir1, cir2 = st.columns((1,2))
        with cir1:
            st.subheader("1)")
            st_lottie(cirt, width=200)
        with cir2:
            st.subheader("EXPLORATORY DATA ANALYSIS USING PYTHON LIBRARIES")
            st.markdown("From:- **:blue[Innomatics Research Labs (Hyderabad)]**")
            st.markdown("[View Certificate](https://drive.google.com/file/d/1G0VRQT-HwN9Qs4xr6jbX0OEYpmd43tB9/view?usp=sharing)")
    st.write("---")
    with st.container():
        cir3, cir4 = st.columns((1,2))
        with cir3:
            st.subheader("2)")
            st_lottie(cirt2, width = 200)
        with cir4:
            st.subheader("PYTHON FOR EVERYBODY (Get Started with Python)")
            st.markdown("From:- **:blue[University of MICHIGAN]**(Online from Coursera)")
            st.markdown("[View Certificate](https://drive.google.com/file/d/1r0a0LTMi45Phtd2Ct-vEnCKfS4NBKxHU/view?usp=sharing)")
    st.write("---")
    with st.container():
        cir5, cir6 = st.columns((1,2))
        with cir5:
            st.subheader("3)")
            st_lottie(cirt3, width = 200)
        with cir6:
            st.subheader("Agile	Methodology	Virtual	Experience Program")
            st.markdown("From:- **:blue[COGNIZANT]**(Online from Forage)")
            st.markdown("[View Certificate](https://drive.google.com/file/d/16nHZl9g9BEeh9KfacD8jXywL9_LLak0m/view?usp=sharing)")
    st.write("---")
    with st.container():
        cir7, cir8 = st.columns((1,2))
        with cir7:
            st.subheader("4)")
            st_lottie(cirt4, width = 200)
        with cir8:
            st.subheader("ChatGPT for Biginners")
            st.markdown("From:- **:blue[Great Learning Academy]**(Online)")
            st.markdown("[View Certificate](https://drive.google.com/file/d/1V1DuC9HL9B4FdypAYlOvq2Ys-adpJvxO/view?usp=sharing)")

        




    
if selected == "Contact":
    st.header("Get in Touch")
    st.write("##")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/rajgubbala09@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" requried> 
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name ="message" placeholder="Your message" requried></textarea>
     <button type="submit">Send</button>
     </form>
    """
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact)

