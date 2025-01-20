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

img01 = pil.Image.open('img1.png')

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
    col03.image(img01, use_column_width=True)
    #daily_input = col01.selectbox('Select Location:', ['U.S.A.','California','Mid Atlantic', 'Mid West', 'North East', 'South East', 'Texas'], key='daily_input')
    daily_input = col01.selectbox('Select Location:', ['U.S.A.'], key='daily_input')
    est_tz = timezone("EST")
    if datetime.datetime.now().astimezone(est_tz) > datetime.datetime.now().astimezone(est_tz).replace(hour=22, minute=30):
        current = datetime.date.today()
    else:
        current = datetime.date.today() - datetime.timedelta(days=1)
    date = col01.date_input("Enter Date:", current, max_value=current, min_value = datetime.date(2024,1,1))

    if (daily_input=='U.S.A.'):
        col11, col12, col13, col14 = my_expander1.columns([0.5,7.5,7.5,0.5])
        col11.markdown("")
        col11.markdown("")
        col14.markdown("")
        col14.markdown("")


        #object1 = bucket.Object(f"daily_conus/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png")
        #object2 = bucket.Object(f"daily_diff/{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_vs_baseline_TROPOMI_ratio.png")
        #response1 = object1.get()
        #response2 = object2.get()
        #file_stream1 = response1['Body']
        #file_stream2 = response2['Body']
        #img1 = pil.Image.open(file_stream1)
        #img2 = pil.Image.open(file_stream2)
        #col12.image(img1, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
        #col13.image(img2, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} versus Baseline Ratio")
        col12.image(f'./daily_data/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_QA75.png', use_column_width = True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")
        col13.image(f'./daily_data/{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_vs_baseline_TROPOMI_ratio.png', use_column_width = True, caption = f"TROPOMI NO2 {daily_input} {date} versus Baseline Ratio")

    elif (daily_input=='California'):
        col11, col12, col13 = my_expander1.columns([3,3,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

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
        object = bucket.Object(f"daily_texas/TROPOMI_{date.strftime('%m')}{date.strftime('%d')}{date.strftime('%Y')}_TX_QA75.png")
        response = object.get()
        file_stream = response['Body']
        img = pil.Image.open(file_stream)
        col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {daily_input} {date} 13:30 Local Time")

    col001, col002, col003 = my_expander1.columns([3,10,3])
    col001.markdown("")
    col001.markdown("")
    col003.markdown("")
    col003.markdown("")
    col002.markdown("<ul style='text-align: justify'>Images pre-dating January 1, 2024 can be found <a href= 'https://gwu.box.com/s/sir2kp9kl6tn1y40yzfig7b9x8acg0kd', target='_blank'>here</a>. The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. 'p' on the image represents one of the top 50 largest NOx-emitting power plants. Data shown here are from the Version 2.4 NO2 algorithm developed by <a href= 'https://sentinels.copernicus.eu/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col002.text("")


##########################################################################################################################

@app.addapp(title='Seasonal TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander1 = st.expander('Seasonal TROPOMI NO2', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img01, use_column_width=True)
    seasonal_input = col01.selectbox('Select Season:', ['Winter', 'Spring', 'Summer', 'Fall'], key='seasonal_input')
    if (seasonal_input=='Winter'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2019', '2020', '2021', '2022', '2023', '2024'], key='year_input')

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

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2018', '2019', '2020', '2021', '2022', '2023', '2024'], key='year_input')
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

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2019', '2020', '2021', '2022', '2023', '2024'], key='year_input')
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

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2018', '2019', '2020', '2021', '2022', '2023'], key='year_input')
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
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Sep-Nov) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    
    col11, col12, col13 = my_expander1.columns([3,10,3])
    col11.markdown("")
    col11.markdown("")
    col13.markdown("")
    col13.markdown("")
    col12.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.4 NO2 algorithms developed by <a href= 'https://sentinels.copernicus.eu/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File', target='_blank'>KNMI</a>. CONUS NRT data are available on this website at 10:30 PM ET each day and displayed until 10:30 PM the next day. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col12.text("")

##########################################################################################################################

@app.addapp(title='Global TROPOMI NO2')
def DailyTROPOMINO2():
    my_expander1 = st.expander('Seasonal TROPOMI NO2', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img01, use_column_width=True)
    seasonal_input = col01.selectbox('Select Season:', ['Annual'], key='seasonal_input')
    #seasonal_input = col01.selectbox('Select Season:', ['Winter', 'Spring', 'Summer', 'Fall','Annual'], key='seasonal_input')

    if (seasonal_input=='Annual'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")
        year_input = col01.selectbox('Select Year:', ['2019', '2020', '2021', '2022', '2023'], key='year_input')

        #object = bucket.Object(f"global/TROPOMI_{year_input}.png")
        #response = object.get()
        #file_stream = response['Body']
        #img = pil.Image.open(file_stream)
        #col12.image(img, use_column_width= True, caption = f"TROPOMI NO2 {seasonal_input} Hotspots in {year_input}")
        col12.image(f'./TROPOMI_{year_input}.png', use_column_width = True)
        
    if (seasonal_input=='Winter'):
        col11, col12, col13 = my_expander1.columns([3,10,3])
        col11.markdown("")
        col11.markdown("")
        col13.markdown("")
        col13.markdown("")

        year_input = col01.selectbox('Select Year (Spring 2020 and beyond have difference plots):', ['2019', '2020', '2021', '2022', '2023'], key='year_input')

        if year_input in ['2019', '2020','2021', '2022', '2023']:
            object = bucket.Object(f"global/tropomi_no2_v24_DJF{year_input}_global_coarse.png")#(f"global/TROPOMI_{year_input}.png")
            #object = bucket.Object(f"global/TROPOMI_{year_input}.png")
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

            object = bucket.Object(f"global/tropomi_no2_v24_DJF{year_input}_global_coarse.png")
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

        year_input = col01.selectbox('Select Year', ['2019', '2020', '2021', '2022', '2023'], key='year_input')
        if year_input in ['2019','2020', '2021', '2022', '2023']:
            object = bucket.Object(f"global/tropomi_no2_v24_JJA{year_input}_global_coarse.png")
            #object = bucket.Object(f"global/TROPOMI_{year_input}.png")
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

            object = bucket.Object(f"global/tropomi_no2_v24_JJA{year_input}_global_coarse.png")
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

        year_input = col01.selectbox('Select Year:', ['2019', '2020', '2021', '2022', '2023'], key='year_input')
        if year_input in ['2019','2020', '2021', '2022', '2023']:
            object = bucket.Object(f"global/tropomi_no2_v24_MAM{year_input}_global_coarse.png")
            #object = bucket.Object(f"global/TROPOMI_{year_input}.png")
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

        year_input = col01.selectbox('Select Year:', ['2018', '2018', '2019', '2020', '2021', '2022', '2023', '2023'], key='year_input')
        if year_input in ['2018', '2019','2020', '2021', '2022', '2023']:
            object = bucket.Object(f"global/tropomi_no2_v24_SON{year_input}_global_coarse.png")
            #object = bucket.Object(f"global/TROPOMI_{year_input}.png")
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
            col15.image(img_t, use_column_width= True, caption=f"TROPOMI NO2 {seasonal_input}(Sep-Nov) {year_input}")
            col16.image(img_b, use_column_width= True, caption=f"Difference between selected timeframe and baseline period")

    
    col11, col12, col13 = my_expander1.columns([3,10,3])
    col11.markdown("")
    col11.markdown("")
    col13.markdown("")
    col13.markdown("")
    col12.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.4 NO2 algorithms developed by <a href= 'https://sentinels.copernicus.eu/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col12.text("")


##########################################################################################################################

@app.addapp(title='Trends Over Time')
def TrendsOverTime():

    my_expander1 = st.expander('Trends Over Time', expanded=True)
    col01, col02, col03 = my_expander1.columns([3,3,3])
    col03.image(img01, use_column_width=True)

    col1, col2, col3 = my_expander1.columns([1,7,1])
    col2.text("")
    col2.text("")

    #object = bucket.Object(f"monthly/Lineplot_TROPOMI_cities_QA75.png")
    #response = object.get()
    #file_stream = response['Body']
    #img = pil.Image.open(file_stream)
    #col2.image(img, use_column_width = True, caption=f"")
    col2.image('./Lineplot_TROPOMI_cities_QA75.png', use_column_width = True)
    
    col2.text("")
    col2.markdown("TROPOMI NO2 urban trends during summer averaged within a 30 km radius of the city center. Bigger size of dot means more cloud-free scenes during that month.")
    col2.text("")
    col2.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    col2.text("")

##########################################################################################################################

# @app.addapp(title='Global Trends Over Time')
# def TrendsOverTime():

#     my_expander1 = st.expander('Trends Over Time', expanded=True)
#     col01, col02, col03 = my_expander1.columns([3,3,3])
#     col03.image(img01, use_column_width=True)

#     col1, col2, col3 = my_expander1.columns([1,7,1])
#     col2.text("")
#     col2.text("")
#     #object = bucket.Object(f"global/TROPOMI_2019.png")

#     object = bucket.Object(f"global/global_difference.png")
#     response = object.get()
#     file_stream = response['Body']
#     img = pil.Image.open(file_stream)
#     col2.image(img, use_column_width = True, caption=f"")
#     col2.text("")
#     #global_difference
#     col2.markdown("Percent Change in annual TROPOMI NO2 averaged over GHS-SMOD urban boundaries for areas with population greater than 500,000.")
#     col2.text("")
#     col2.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.2 and 2.3.1 NO2 algorithms developed by <a href= 'https://amt.copernicus.org/articles/15/2037/2022/', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
#     col2.text("")

##########################################################################################################################

@app.addapp(title='Annual City Zoom-ins', is_home=True)
def About():
    my_expander3 = st.expander('About', expanded=True)
    col01, col02, col03 = my_expander3.columns([3,3,3])
    
    my_expander3.markdown("<p style='text-align: justify;'>This website displays NO2 tropospheric vertical column amounts observed by TROPOMI over the continental USA, southern Canada and northern Mexico. Data shown are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.4 NO2 algorithms developed by <a href= 'https://sentinels.copernicus.eu/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Please visit our <b>Daily TROPOMI NO2</b> and <b>Seasonal TROPOMI NO2</b> pages for data aggregated over various time intervals.</p>", unsafe_allow_html=True)
    col02.text("")
    col02.text("")

    col03.image(img01, use_column_width=True)
    
    col02.text("")
    col02.text("")
    
    col1, col2, col3 = my_expander3.columns([1,7,1])
    col2.text("")
    col2.image('./TROPOMI_homepage.png', use_column_width = True)

    my_expander3.markdown("<h3 style='text-align: left; font-weight: bold '>More Information:</h1>", unsafe_allow_html=True)
    my_expander3.markdown("<ul style='text-align: justify'>The <a href= 'https://tropomino2.us', target='_blank'>tropomino2.us</a> web site is maintained by the <a href= 'https://blogs.gwu.edu/sanenberg/', target='_blank'>Air Climate and Health Lab</a> at the Milken Institute School of Public Health at George Washington University, and is not directly affiliated with Tropomi Science Team. Data shown on the website are tropospheric vertical column amounts, are filtered to show measurements with a quality assurance flag exceeding 0.75, and are re-gridded using a methodology described in <a href= 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001665', target='_blank'>Goldberg et al. 2021</a>. Daily images are from the near-real-time (NRT) product and the monthly data are from the offline (OFFL) product. Data shown here are from the Version 2.4 NO2 algorithms developed by <a href= 'https://sentinels.copernicus.eu/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File', target='_blank'>KNMI</a>. NRT data are available on this website approximately 3 hours after the measurement. Tropomi NO2 can be downloaded from: <a href= 'http://www.tropomi.eu/data-products/nitrogen-dioxide', target='_blank'>http://www.tropomi.eu/data-products/nitrogen-dioxide</a>", unsafe_allow_html=True)
    my_expander3.text("")

##########################################################################################################################

app.run()
