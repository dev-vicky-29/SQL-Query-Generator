import streamlit as st

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")

    st.markdown(
        """
            <div style="text-align: center">
            <h1>SQL Query Generator</h1>
            <h3>I can Generate SQL Query for You!</h3>
            <h4>With Explanation as Well !!</h4>
            <p>This tool is a simple tool that allows you to Generate SQL Queries based on your Prompts.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    text_input=st.text_area("Enter your Query Here in Plan English:")
    submit=st.button("Generate SQL Query")
if __name__ == "__main__":
    main()
