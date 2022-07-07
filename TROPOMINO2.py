from operator import index
from pickle import TRUE
from tkinter.tix import AUTO
from turtle import title, width
import pandas as pd
import numpy as np
import PIL as pil
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit.elements import layouts
import hydralit as hy
from pytz import timezone
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

# @app.addapp(title='Homepage')
# def Home():
#     my_expander1 = st.expander('Description', expanded=True)  
#     col1, col2, col3 = my_expander1.columns([1,7,1])
#     #col2.markdown("<h3 style='text-align: left; font-weight: bold '>Description:</h1>", unsafe_allow_html=True)
#     col2.markdown("<p style='text-align: justify;'>This website displays NO2 tropospheric vertical column amounts observed by TROPOMI over the continental USA, southern Canada and northern Mexico. Data shown are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Please visit our <b>Daily TROPOMI NO2</b> and <b>Seasonal TROPOMI NO2</b> pages for data aggregated over various time intervals.</p>", unsafe_allow_html=True)

            
#     col2.text("")
#     col2.text("")

#     col2.image('./TROPOMI_homepage.png', use_column_width = True)

##########################################################################################################################

@app.addapp(title='Daily TROPOMI NO2', is_home=True)
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
        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_conus/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
    elif (daily_input=='California'):
        col11, col12, col13 = my_expander1.columns([3,3,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_california/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_CA_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")

    elif (daily_input=='Mid Atlantic'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midAtl/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_midAtl_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")

    elif (daily_input=='Mid West'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_midwest/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_MW_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
    elif (daily_input=='North East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_northeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_EUS_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
    elif (daily_input=='South East'):
        col11, col12, col13 = my_expander1.columns([3,8,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_southeast/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_SE_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
    elif (daily_input=='Texas'):
        col11, col12, col13 = my_expander1.columns([3,7,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        if datetime.datetime.now() > datetime.datetime.now().replace(hour=20, minute=30):
            current = datetime.date.today()
        else:
            current = datetime.date.today() - datetime.timedelta(days=1)
        date = col12.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2022,1,4))
        object = bucket.Object(f"daily_texas/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_TX_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
    #col12.markdown("<ul style='text-align: center'>'p' on the image represents one of the top 50 largest NOx-emitting power plants.", unsafe_allow_html=True)
    #col12.text("")
    col12.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. 'p' on the image represents one of the top 50 largest NOx-emitting power plants. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col12.text("")

##########################################################################################################################

# @app.addapp(title='Monthly TROPOMI NO2')
# def MonthlyTROPOMINO2():

#     def monthnumber(string):
#         m = {
#             'jan': 1,
#             'feb': 2,
#             'mar': 3,
#             'apr':4,
#             'may':5,
#             'jun':6,
#             'jul':7,
#             'aug':8,
#             'sep':9,
#             'oct':10,
#             'nov':11,
#             'dec':12
#             }
#         s = string.strip()[:3].lower()
#         return m[s]

#     my_expander2 = st.expander('Monthly TROPOMI NO2', expanded=True)  
#     col01, col02, col03 = my_expander2.columns([3,3,3])
#     col03.image(img1, use_column_width=True)
#     years = ['2019','2020','2021','2022']
#     default = years.index(datetime.datetime.now().strftime("%Y"))
#     year_input = col01.selectbox('Select Year:', years, key='year_input', index=default)
#     if year_input:
#         months = ['January','February','March','April','May','June','July','August','September','October','November','December']
#         default = months.index((datetime.datetime.now() - datetime.timedelta(days=41)).strftime("%B"))
#         month_input = col01.selectbox('Select Month:', months, key='month_input', index=default)
#         if month_input:
#             col11, col12, col13 = my_expander2.columns([3,8,3])
#             try:
#                 date = datetime.datetime.strptime(month_input, "%B")
#                 object = bucket.Object(f"monthly/{date.strftime('%m')}{year_input}_TROPOMI_QA75.png")
#                 response = object.get()
#                 file_stream = response['Body']
#                 img = pil.Image.open(file_stream)
#                 col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {month_input}, {year_input} 13:30 Local Time")
                
#             except:
#                 col12.text("")
#                 col12.text("")
#                 col12.text("")
#                 col12.markdown("<ul style='text-align: justify; font-size:25px'>Data not yet available.", unsafe_allow_html=True)
#     col12.markdown("<ul style='text-align: center'>'p' on the image represents one of the top 50 largest NOx-emitting power plants.", unsafe_allow_html=True)
#     col12.text("")
#     col12.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3
#  hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)

##########################################################################################################################

@app.addapp(title='Seasonal TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander1 = st.expander('Seasonal TROPOMI NO2', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img1, use_column_width=True)
    seasonal_input = col01.selectbox('Select Season:', ['Winter', 'Spring', 'Summer', 'Fall'], key='seasonal_input')
    if (seasonal_input=='Winter'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2019', '2020', '2021', '2022'], key='year_input')

        if year_input in ['2019', '2020']:
            object = bucket.Object(f"seasonal/DJF_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img = pil.Image.open(file_stream)
            col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {seasonal_input}(Dec-Feb) {year_input}")
        
        else:
            col14, col15, col16, col17 = my_expander1.columns([0.5,9,9,0.5])
            col14.markdown("")
            col14.markdown("")
            col17.markdown("")
            col17.markdown("")

            object = bucket.Object(f"seasonal/DJF_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img_t = pil.Image.open(file_stream)
            object = bucket.Object(f"seasonal/DJF_{year_input}_vs_baseline_TROPOMI_diff.png")
            response = object.get()
            file_stream = response['Body']
            img_b = pil.Image.open(file_stream)
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Dec-Feb) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    elif (seasonal_input=='Summer'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2018', '2019', '2020', '2021'], key='year_input')
        if year_input in ['2018', '2019']:
            object = bucket.Object(f"seasonal/JJA_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img = pil.Image.open(file_stream)
            col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {seasonal_input}(Jun-Aug) {year_input}")
        else:
            col14, col15, col16, col17 = my_expander1.columns([0.5,9,9,0.5])
            col14.markdown("")
            col14.markdown("")
            col17.markdown("")
            col17.markdown("")

            object = bucket.Object(f"seasonal/JJA_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img_t = pil.Image.open(file_stream)
            object = bucket.Object(f"seasonal/JJA_{year_input}_vs_baseline_TROPOMI_diff.png")
            response = object.get()
            file_stream = response['Body']
            img_b = pil.Image.open(file_stream)
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Jun-Aug) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    elif (seasonal_input=='Spring'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2019', '2020', '2021', '2022'], key='year_input')
        if year_input in ['2019']:
            object = bucket.Object(f"seasonal/MAM_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img = pil.Image.open(file_stream)
            col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {seasonal_input}(Mar-May) {year_input}")
        else:
            col14, col15, col16, col17 = my_expander1.columns([0.5,9,9,0.5])
            col14.markdown("")
            col14.markdown("")
            col17.markdown("")
            col17.markdown("")

            object = bucket.Object(f"seasonal/MAM_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img_t = pil.Image.open(file_stream)
            object = bucket.Object(f"seasonal/MAM_{year_input}_vs_baseline_TROPOMI_diff.png")
            response = object.get()
            file_stream = response['Body']
            img_b = pil.Image.open(file_stream)
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Mar-May) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    elif (seasonal_input=='Fall'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2018', '2019', '2020', '2021'], key='year_input')
        if year_input in ['2018', '2019']:
            object = bucket.Object(f"seasonal/SON_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img = pil.Image.open(file_stream)
            col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {seasonal_input}(Sep-Nov) {year_input}")
        else:
            col14, col15, col16, col17 = my_expander1.columns([0.5,9,9,0.5])
            col14.markdown("")
            col14.markdown("")
            col17.markdown("")
            col17.markdown("")

            object = bucket.Object(f"seasonal/SON_{year_input}_TROPOMI_QA75.png")
            response = object.get()
            file_stream = response['Body']
            img_t = pil.Image.open(file_stream)
            object = bucket.Object(f"seasonal/SON_{year_input}_vs_baseline_TROPOMI_diff.png")
            response = object.get()
            file_stream = response['Body']
            img_b = pil.Image.open(file_stream)
            images = [img_t, img_b]
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Sep-Nov) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    
    col11, col12, col13 = my_expander1.columns([3,10,3])
    col11.markdown("")
    col11.markdown("")
    col13.markdown("")
    col13.markdown("")
    #col12.markdown("<ul style='text-align: center'>'p' on the image represents one of the top 50 largest NOx-emitting power plants.", unsafe_allow_html=True)
    #col12.text("")
    col12.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col12.text("")

##########################################################################################################################

@app.addapp(title='Trends Over Time')
def TrendsOverTime():

    my_expander1 = st.expander('Trends Over Time', expanded=True)  
    col1, col2, col3 = my_expander1.columns([1,7,1])
    col2.text("")
    col2.text("")

    object = bucket.Object(f"monthly/Lineplot_TROPOMI_cities_QA75.png")
    response = object.get()
    file_stream = response['Body']
    img = pil.Image.open(file_stream)
    col2.image(img, use_column_width = True, caption=f"")

    col2.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col2.text("")

##########################################################################################################################

@app.addapp(title='About')
def About():
    my_expander3 = st.expander('About', expanded=True)
    col01, col02, col03 = my_expander3.columns([3,3,3])
    
    my_expander3.markdown("<p style='text-align: justify;'>This website displays NO2 tropospheric vertical column amounts observed by TROPOMI over the continental USA, southern Canada and northern Mexico. Data shown are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Please visit our <b>Daily TROPOMI NO2</b> and <b>Seasonal TROPOMI NO2</b> pages for data aggregated over various time intervals.</p>", unsafe_allow_html=True)
    col03.image(img1, use_column_width=True)
    col02.text("")
    col02.text("")

    col1, col2, col3 = my_expander3.columns([1,7,1])
    col2.text("")
    col2.text("")
    col2.image('./TROPOMI_homepage.png', use_column_width = True)

    my_expander3.markdown("<h3 style='text-align: left; font-weight: bold '>More Information:</h1>", unsafe_allow_html=True)
    my_expander3.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    my_expander3.text("")

##########################################################################################################################

app.run()