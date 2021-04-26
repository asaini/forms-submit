import streamlit as st
import time

my_bar = st.progress(0)
time.sleep(1)
my_bar.progress(100)

# Using Prototype Streamlit, version 0.79.0

st.sidebar.title('Sidebar')

form = st.sidebar.form('sidebar-form')
name = form.text_input('Enter your name')
sidebar_submit = form.form_submit_button('Submit')
st.sidebar.write('Press submit to have your name printed below')
if sidebar_submit:
    st.sidebar.write(f'hello {name}')


st.title('Multiple Submit Buttons')
with st.echo():
    # Note: You have to click the submit button for the checkbox log to take effect!
    with st.form('multiple-submit-buttons'):
        checkbox = st.checkbox('Check to have 2 submit buttons')
        if checkbox:
            submit1 = st.form_submit_button('Submit1')
            submit2 = st.form_submit_button('Submit2')
        else:
            submit1 = st.form_submit_button('Submit1')

st.markdown('---')
st.title('Forms in 2 Columns')

with st.echo():
    col1, col2 = st.beta_columns(2)

    with col1:
        with st.form('Form1'):
            st.selectbox('click', ['click', 'or click'], key=1)
            st.slider(label='Slider1', min_value=0, max_value=100, key=4)
            submitted1 = st.form_submit_button('Submit 1')

    with col2:
        with st.form('Form2'):
            st.selectbox('click', ['click', 'or click'], key=2)
            st.slider(label='Slider2',min_value=0, max_value=100, key=3)
            submitted2 = st.form_submit_button('Submit 2')

st.markdown('---')

st.title('Multiple columns in Form')

with st.echo():
    counti = 0
    with st.form('test loop'):
        cols=st.beta_columns(5)
        for col in cols:
            col.selectbox(f'click{counti}', ['click', 'or click'], key=counti)
            counti += 1
        submitted = st.form_submit_button('Submit')


st.markdown('---')


st.title('File Uploader in Forms')

st.subheader('Single File')
with st.echo():
    with st.form('single_file_uploader'):
        uploaded_file = st.file_uploader('myuploader')
        fu_submit = st.form_submit_button('Submit')
    st.write(f'Uploaded file: {uploaded_file}')

st.subheader('Multiple Files')
with st.echo():
    with st.form('multiple_file_uploader'):
        uploaded_files = st.file_uploader('myuploader', accept_multiple_files=True)
        fu_submit = st.form_submit_button('Submit')

    for file in uploaded_files:
        st.write(f'Uploaded file: {file}')

st.markdown('---')

st.title('Missing submit button')

st.subheader('Using a with clause only')

with st.echo():
    with st.form('simple_with'):
        slider = st.slider('enter a number', 1, 100, 40)

st.write(f'This is the slider value= {slider}')

st.subheader('Using the form assignment clause')

with st.echo():
    a = st.form('form_assignement')
    a.text_input('Enter some text')


st.subheader('Combination of with and form assigmnent')


with st.echo():
    a = st.form('combination')

    with a:
        text = st.text_input('Enter some text')

    a.text_area('Enter a text area')

st.markdown('---')

st.title('Missing Form but having a submit button')

st.code('''
# Submit button without a form
my_submit = st.form_submit_button('My submit')''', language='python')

st.write('We want this to throw an exception!')

with st.echo():
    my_submit = st.form_submit_button('My submit')



