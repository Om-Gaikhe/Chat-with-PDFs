import streamlit as st

def main():
    st.set_page_config(page_title="Talk about PDFs", page_icon=':Books:')

    st.header("Talk about PDFs :Books:")
    st.text_input("Ask question about the documens:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and hit Process")
        st.botton("Process")



if __name__ == 'main':
    main()