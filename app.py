import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCsP_1IId2hByQPak9a5_lPZbpJyHFTF6o"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")

    st.markdown(
        """
            <div style="text-align: center">
            <h1>🛢️👨🏼‍💻 SQL Query Generator 🛢️👨🏼‍💻</h1>
            <h3>I can Generate SQL Query for You!</h3>
            <h4>With Explanation as Well !!</h4>
            <h5>Developed By 
            <a target="_blank" href="https://www.linkedin.com/in/shruti-patil-7676a724a/">Shruti Patil</a> & 
            <a target="_blank" href="https://www.linkedin.com/in/dev-vicky-29j/">Vivek Deshmukh</a></h5>
            <p>This tool is a simple tool that allows you to Generate SQL Queries based on your Prompts.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    text_input=st.text_area("Enter your Query Here in Plan English:")

    submit=st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                Create a SQL Query Snippet using the below text:
                ```
                    {text_input}
                ```
                I just want a SQL Query.
            """

            formatted_template=template.format(text_input=text_input)
            response=model.generate_content(formatted_template)
            sql_query=response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
        
            expacted_output="""
                What would be the expected response of this SQL Query Snippet:
                ```
                    {sql_query}
                ```
                Provide sample tabular Response with no explaination.
            """
            expacted_output_formatted=expacted_output.format(sql_query=sql_query)
            eoutput=model.generate_content(expacted_output_formatted)
            eoutput=eoutput.text

            explaination="""
                Explain this SQL Query:
                ```
                    {sql_query}
                ```
                Please Provide With simplest of explaination.
            """
            explaination_formatted=explaination.format(sql_query=sql_query)
            explaination=model.generate_content(explaination_formatted)
            explaination=explaination.text

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code(sql_query, language="sql")

                st.success("Expected Output of this SQL Query will be:")
                st.markdown(eoutput)

                st.success("Explaination of this SQL Query")
                st.markdown(explaination)

        

if __name__ == "__main__":
    main()
