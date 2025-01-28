import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCsP_1IId2hByQPak9a5_lPZbpJyHFTF6o"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="Query Generator", page_icon=":robot:")

    st.markdown(
        """
            <div style="text-align: center">
            <h1>🛢️👨🏼‍💻 Query Generator 🛢️👨🏼‍💻</h1>
            <h3>I can Generate Queries for You!</h3>
            <h4>With Explanation as Well !!</h4>
            <h5>Developed By 
             <a target="_blank" href="https://www.linkedin.com/in/shruti-patil-7676a724a/">Shruti Patil</a> & 
            <a target="_blank" href="https://www.linkedin.com/in/dev-vicky-29j/">Vivek Deshmukh</a></h5>
            <p>This tool is a simple tool that allows you to Generate Queries based on your Prompts.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

    database = st.selectbox("Select Database", ["SQL", "PostgreSQL", "MongoDB", "Oracle"])
    text_input = st.text_area("Enter your Query Here in Plain English:")

    submit = st.button("Generate Query")
    if submit:
        with st.spinner("Generating Query..."):
            if database == "SQL":
                template = """
                    Create a SQL Query Snippet using the below text:
                    ```
                        {text_input}
                    ```
                    I just want a SQL Query.
                """
            elif database == "PostgreSQL":
                template = """
                    Create a PostgreSQL Query Snippet using the below text:
                    ```
                        {text_input}
                    ```
                    I just want a PostgreSQL Query.
                """
            elif database == "MongoDB":
                template = """
                    Create a MongoDB Query Snippet using the below text:
                    ```
                        {text_input}
                    ```
                    I just want a MongoDB Query.
                """
            elif database == "Oracle":
                template = """
                    Create an Oracle SQL Query Snippet using the below text:
                    ```
                        {text_input}
                    ```
                    I just want an Oracle SQL Query.
                """

            formatted_template = template.format(text_input=text_input)
            response = model.generate_content(formatted_template)
            query = response.text.strip().strip("```sql").strip("```").strip()

            expacted_output = f"""
                What would be the expected response of this {database} Query Snippet:
                ```
                    {query}
                ```
                Provide sample tabular Response with no explanation.
            """
            eoutput = model.generate_content(expacted_output).text.strip()

            explaination = f"""
                Explain this {database} Query:
                ```
                    {query}
                ```
                Please provide the simplest explanation.
            """
            explanation = model.generate_content(explaination).text.strip()

            with st.container():
                st.success(f"{database} Query Generated Successfully! Here is your Query Below:")
                st.code(query, language="sql" if database in ["SQL", "PostgreSQL", "Oracle"] else "json")

                st.success("Expected Output of this Query will be:")
                st.markdown(eoutput)

                st.success("Explanation of this Query")
                st.markdown(explanation)

if __name__ == "__main__":
    main()
