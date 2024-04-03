import streamlit as st

def main():
    st.title('Contact Us')

    st.write('Please fill out the form below to get in touch with us.')

    name = st.text_input('Name')
    email = st.text_input('Email')

    message = st.text_area('Message', height=200)

    category = st.selectbox('Category', ['General Inquiry', 'Technical Support', 'Sales', 'Feedback'])

    subscribe = st.checkbox('Subscribe to Newsletter')

    if st.button('Submit'):
        # You can add your custom logic here to handle the form submission, such as sending an email or saving to a database
        st.success('Thank you for reaching out. We will get back to you soon.')
        st.write('Name:', name)
        st.write('Email:', email)
        st.write('Message:', message)
        st.write('Category:', category)
        if subscribe:
            st.write('Subscribed to Newsletter')

if __name__ == '__main__':
    main()
