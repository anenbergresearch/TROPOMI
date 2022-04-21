from operator import index
import pandas as pd
import numpy as np
import PIL as pil
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit.elements import layouts
import hydralit as hy
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id = st.secrets["aws_access_key_id"],
    aws_secret_access_key = st.secrets["aws_secret_access_key"],
    region_name = 'us-east-1'
)
bucket = s3.Bucket('tropomino2')


st.set_page_config(page_title="TROPOMI NO2", layout= "wide")
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

##########################################################################################################################
img1 = pil.Image.open('img1.png')
#col01, col02, col03 = st.columns([2,4,2])
#col02.image(img1, use_column_width=True)


over_theme = {'txc_inactive': '#000000'}
app = hy.HydraApp(title='TROPOMINO2',
        hide_streamlit_markers=False,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )


##########################################################################################################################

@app.addapp(title='Daily TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander1 = st.expander('Daily TROPOMI NO2', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    daily_input = col01.selectbox('Select Location:', ['U.S.A.','California','Mid Atlantic', 'Mid West', 'North East', 'South East', 'Texas'], key='daily_input')
    if (daily_input=='U.S.A.'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_conus/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='California'):
        col11, col12, col13 = my_expander1.columns([3,3,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_california/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_CA_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")

    elif (daily_input=='Mid Atlantic'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midAtl/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_midAtl_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")

    elif (daily_input=='Mid West'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midwest/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_MW_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='North East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_northeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_EUS_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='South East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_southeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_SE_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    elif (daily_input=='Texas'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        date = col12.date_input("Enter Date:", datetime.date.today() - datetime.timedelta(days=1), max_value=datetime.date.today() - datetime.timedelta(days=1), min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_texas/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_TX_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date}")
    
    



##########################################################################################################################

@app.addapp(title='Monthly TROPOMI NO2')
def MonthlyTROPOMINO2():

    def monthnumber(string):
        m = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr':4,
            'may':5,
            'jun':6,
            'jul':7,
            'aug':8,
            'sep':9,
            'oct':10,
            'nov':11,
            'dec':12
            }
        s = string.strip()[:3].lower()
        return m[s]

    my_expander2 = st.expander('Monthly TROPOMI NO2', expanded=True)  
    col01, col02, col03 = my_expander2.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    years = ['2019','2020','2021','2022']
    default = years.index(datetime.datetime.now().strftime("%Y"))
    year_input = col01.selectbox('Select Year:', years, key='year_input', index=default)
    if year_input:
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        default = months.index((datetime.datetime.now() - datetime.timedelta(days=20)).strftime("%B"))
        month_input = col01.selectbox('Select Month:', months, key='month_input', index=default)
        if month_input:
            col11, col12, col13 = my_expander2.columns([3,8,3])
            try:
                date = datetime.datetime.strptime(month_input, "%B")
                object = bucket.Object(f"monthly/{date.strftime('%m')}{year_input}_TROPOMI_QA75.png")
                response = object.get()
                file_stream = response['Body']
                img = pil.Image.open(file_stream)
                col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {month_input}, {year_input}")
                
            except:
                col12.text("")
                col12.text("")
                col12.text("")
                col12.markdown("<ul style='text-align: justify; font-size:25px'>Data not yet available.", unsafe_allow_html=True)


@app.addapp(title='About')
def About():
    my_expander3 = st.expander('About', expanded=True)
    col01, col02, col03 = my_expander3.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    my_expander3.markdown("<h3 style='text-align: left; font-weight: bold '>More Information:</h1>", unsafe_allow_html=True)
    my_expander3.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 5 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)

app.run()





