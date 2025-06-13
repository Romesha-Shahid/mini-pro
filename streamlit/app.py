import sreamlit as st  # type: ignore
import pandas as pd # type: ignore
import io import BytesIO # type: ignore

#Set up  our App
st.set_page_config(page_title="Data SWeeper",layout='wide')
st.title("Data sweeper")
st.write("Transfrom your files betwween CSV and Excel formats with built-in data cleaning and  visualization!")

uploaded_file = st.file_uploader("Upload you files (CSV or E Excel):", type=["csv", "xlsx"],accept_multiple_file=True)

if uploaded_file:
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower() # type: ignore
        
        if file_ext == ".csv":
            df =  pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type : {file_ext}")
            continue

        #Display info about the file 

        st.write(f"**File Name:**{file.name}")
        st.write(f"**File Size:**{file.size}")
        
        # Show 5 rows of our df
        st.write("Preveiw the Head of the Dataframe")
        st.dataframe(df.head())

        # Options for data cleaning
        st.subheader("Data Cleaning Option")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2  = st.columns(2)

            with col1:
                if st.button(f"Remove  Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

                    with col2:
                        if st.button(f"Fill Missing Value for {file.name}"):
                            numeric_cols = df.select_dtypes(include=['number']).column
                            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                            st.write("Missing Value have been Failed!")

                            # Choose Spefic Column to Keep or Convert
                            st.subheader("Select Columns to convert")
                            columns = st.multiselect(f"choose columns for {file.name}",df.columns, defualt=df.columns)
                            df = df[columns]

                            # Create some Visualizations
                            st.subheader("Data Viusalization")
                            if st.checkbox(f"Show Viusalization for {file.name}"):
                                st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
                                

                                # Convert the file CSV to Excel
                                st.subheader("Conversion Options")
                                conversion_type =st.radio(f"Convert{file.name} to:", ["CSV","Excel"], key=file.name)
                                if st.button(f"Convert{file.name}"):
                                    buffer = BytesIO()
                                if conversion_type == "CSV":
                                        df.to_csv(buffer,index=False)
                                        file_name = file.name.replace(file_ext, ".csv")
                                        mime_type = "text/csv"

                                elif conversion_type == "Excel":
                                    df.to_excel(buffer, index=False)
                                    file_name = file.name.replace(file_ext,".xlsx")
                                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                                    buffer.seek(0)

                                    # Download Button
                                    st.download_button(
                                        label=f"Download{file.name} as {conversion_type}",
                                        data=buffer,
                                        filename=file_name,
                                        mime=mime_type
                                    )
                            st.succes("All files processeed")
                            
                                        

                                