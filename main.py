import streamlit as st
from groq import Groq

def predict_depression_level(input_text):
    groq_api_key = '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'  # Groq API key
    client = Groq(api_key=groq_api_key)
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {   
                "role": "system",
                "content": "You are a mental health prediction system designed to assess and categorize the level of depression based on the given text input. You will categorize depression into four levels: minimum, mild, moderate, and severe. Additionally, you will rate the depression on a scale of 1 to 10, with 1 being the least or no depression and 10 being the highest level of depression."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    prediction = ""
    for chunk in completion:
        prediction += chunk.choices[0].delta.content or ""
    return prediction

def main():
    st.title("🧠Mental LLM")
    input_text = st.text_area("Enter your text here:")
    if st.button("Predict"):
        prediction = predict_depression_level(input_text)
        st.write("Prediction:")
        st.write(prediction)

if __name__ == "__main__":
    main()


# import streamlit as st
# from groq import Groq
# import time

# def predict_depression_level(input_text):
#     groq_api_key = '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'  # Groq API key
#     client = Groq(api_key=groq_api_key)
#     completion = client.chat.completions.create(
#         model="gemma-7b-it",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a mental health prediction system. Based on the given prompt, you have to categorize into three mild, moderate, and severe depression and also rate it on a scale of 1 to 10. 1 being least or no depression and 10 being the highest level of depression."
#             },
#             {
#                 "role": "user",
#                 "content": input_text
#             }
#         ],
#         temperature=1,
#         max_tokens=1024,
#         top_p=1,
#         stream=True,
#         stop=None,
#     )

#     prediction = ""
#     for chunk in completion:
#         prediction += chunk.choices[0].delta.content or ""
#     return prediction

# def main():
#     st.set_page_config(page_title="Mental Health Prediction System", page_icon=":brain:", layout="wide")

#     # Custom CSS
#     st.markdown("""
#         <style>
#         body {
#             background-color: #000;
#             color: #333333;
#         }
#         .stApp {
#             background-color: #f0f2f6;
#         }
#         .title {
#             font-size: 2.5em;
#             color: #4a4a4a;
#         }
#         .text-area {
#             background-color: #ffffff;
#             border-radius: 5px;
#             padding: 10px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         }
#         .button {
#             background-color: #000;
#             color: white;
#             padding: 10px 24px;
#             text-align: center;
#             font-size: 16px;
#             margin: 10px 2px;
#             cursor: pointer;
#             border: none;
#             border-radius: 5px;
#         }
#         .button:hover {
#             background-color: #45a049;
#         }
#         .prediction {
#             font-size: 1.2em;
#             color: #333333;
#             background-color: #ffffff;
#             padding: 10px;
#             border-radius: 5px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         }
#         .example-prompts {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #ffffff;
#             border-radius: 5px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     st.title("🧠 Mental Health Prediction System")
#     st.markdown("Welcome to the Mental Health Prediction System. Enter your text below to get a prediction on the level of depression.")

#     col1, col2 = st.columns([2, 1])

#     with col1:
#         input_text = st.text_area("Enter your text here:", height=200, class_="text-area")
#         if st.button("Predict", key="predict_button", help="Click to predict the level of depression", class_="button"):
#             if input_text.strip() == "":
#                 st.error("Please enter some text before predicting.")
#             else:
#                 with st.spinner("Analyzing..."):
#                     prediction = predict_depression_level(input_text)
#                     time.sleep(2)  # Simulate processing time
#                     st.markdown("## Prediction:")
#                     st.markdown(f"<div class='prediction'>{prediction}</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown("### Example Prompts", class_="example-prompts")
#         st.markdown("""
#         - "I have been feeling pretty good lately, but sometimes I get a little anxious about work. Overall, I think I'm doing okay."
#         - "I've been feeling a bit down for the past few weeks. I still go to work and do my chores, but I don't feel as motivated as I used to."
#         - "Lately, I've been struggling to get out of bed in the morning. I find it hard to concentrate at work, and I feel overwhelmed by small tasks."
#         - "I feel hopeless and can't see a way out of my sadness. I have trouble sleeping, and I don't have the energy to do anything."
#         """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("### About")
#     st.markdown("This application uses the gemma-7b-it model from Groq to analyze text and predict the level of depression. The model categorizes the input into mild, moderate, or severe depression and rates it on a scale of 1 to 10, with 1 being the least or no depression and 10 being the highest level of depression.")

# if _name_ == "_main_":
#     main()