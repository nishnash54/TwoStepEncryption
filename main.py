import os
import sys
sys.path.insert(0, './src')

import streamlit as st

from PIL import Image
from src.lsb_stegno import lsb_encode, lsb_decode
from src.n_share import generate_shares, compress_shares

menu = st.sidebar.radio('Options', ['Docs', 'Encode', 'Decode'])

if menu == 'Docs':
    st.title('Documentation')
    with open('README.md', 'r') as f:
        docs = f.read()
    st.markdown(docs, unsafe_allow_html=True)

elif menu == 'Encode':
    st.title('Encoding')

    # Image
    img = st.file_uploader('Upload image file', type=['jpg', 'png', 'jpeg'])
    if img is not None:
        img = Image.open(img)
        try:
            img.save('images/img.jpg')
        except:
            img.save('images/img.png')
        st.image(img, caption='Selected image to use for data encoding',
                use_column_width=True)

    # Data
    txt = st.text_input('Message to hide')

    # Encode message
    if st.button('Encode data and Generate shares'):

        # Checks
        if len(txt) == 0:
            st.warning('No data to hide')
        elif img is None:
            st.warning('No image file selected')

        # Generate splits
        else:
            generate_shares(lsb_encode(txt))
            try:
                os.remove('images/img.jpg')
            except FileNotFoundError:
                os.remove('images/img.png')
            st.success('Data encoded, Shares generated in folder [images]')

elif menu == 'Decode':
    st.title('Decoding')

    # Share 1
    img1 = st.file_uploader('Upload Share 1', type=['png'])
    if img1 is not None:
        img1 = Image.open(img1)
        img1.save('images/share1.png')
        st.image(img1, caption='Share 1', use_column_width=True)

    # Share 2
    img2 = st.file_uploader('Upload Share 2', type=['png'])
    if img2 is not None:
        img2 = Image.open(img2)
        img2.save('images/share2.png')
        st.image(img2, caption='Share 2', use_column_width=True)

    # Decode message
    if st.button('Compress shares and Decode message'):

        # Check
        if img1 is None or img2 is None:
            st.warning('Upload both shares')

        # Compress shares
        else:
            compress_shares()
            os.remove('images/share1.png')
            os.remove('images/share2.png')
            st.success('Decoded message: ' + lsb_decode('images/compress.png'))

