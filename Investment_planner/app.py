import json
import streamlit as st 
import google.generativeai as genai
st.title("Investment Planner")
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

col1, col2 = st.columns(2)
with col1:
    goal = st.selectbox(' What is your primary financial goal?', ('Saving for retirement', 'Building an emergency fund', 'Buying a house','Paying for a child\'s education','Taking a dream vacation'))
    income = st.number_input('What is your current income level?')
    
with col2:
    time = st.selectbox('What is your investment time horizon?', ('Short-term (Less than 5 years)', 'Medium-term (5-10 years)', 'Long-term (10+ years)'))
    debt = st.selectbox(' Do you have any existing debt?', ('Yes', 'No'))

invest = st.number_input('How much investable money do you have available?')
scale= st.slider("How comfortable are you with risk?", min_value=1, max_value=10,step=1)
 
user_data = f""" - Primary financial goal is  {goal}"
                - My current income level in INR {income} Ruppes"
                - My investment time horizon {time} years old"
                - And my details about status is {debt}"
                - How much investable money do you have available is {invest} on INR
                - comfortable are you with risk{scale} out of 10? """

output_format = """ "Understanding Your Situation":"Short-term Goal: Retirement planning is usually a long-term goal. With a horizon of less than 5 years, you'd typically want to prioritize capital preservation over aggressive growth.
Modest Risk Tolerance: A 5 out of 10 risk score suggests a preference for less volatile investments.
Small Investable Amount: This limits the diversification options you might have.",
                    "Investment Options & Potential Allocation":"High-Yield Savings Account/Short-Term Fixed Deposit (50%):  Since your time horizon is short, it's crucial to keep a significant portion in easily accessible and safe options. This preserves your money while earning some interest.

Liquid Funds (20%): These mutual funds invest in very short-term debt securities. They offer slightly higher potential returns than savings accounts, with relatively low risk and good liquidity.

Conservative Hybrid Mutual Funds (20%): These funds invest in a mix of debt and equity, offering a balance of potential growth and some stability. Look for funds with a higher debt allocation.

Blue-chip Stocks/Index Funds (10%): A small portion in reliable, large-company stocks or an index fund can provide some exposure to long-term growth potential. However, the short time horizon means the stock market might be too risky for a larger portion of your investment.",
                    "Important Considerations":"NO Crypto: Cryptocurrencies are extremely volatile and don't align with your goals of capital preservation and modest risk in a short timeframe.
Limited US Stocks: Investing in US stocks directly comes with currency exchange risks and might be complicated with smaller investment amounts.
Gold: Gold can act as a hedge against inflation, but its short-term price fluctuations can be significant. Consider it only if you have a slightly longer investment horizon.",
                
                    "Disclaimer": I\'m an AI chatbot, not a financial advisor. This information is for educational purposes only and should not replace professional advice.",
                                    """
prompt = user_data + (" Based on Above Details Suggest Investment Plan and Output is return in JSON only and take only reference is ") + output_format 
 
if st.button("Generate Investment Plan"):
    with st.spinner('Creating Investmentl plan'):
        text_area_placeholder = st.empty()
        
        meal_plan = generate_text_openai_streamlit(client, prompt, model="gpt-4-0125-preview",
                                                   text_area_placeholder=text_area_placeholder)
        # Check if the string starts with ```json and remove it
        if meal_plan.startswith("```json"):
            meal_plan = meal_plan.replace("```json\n", "", 1)  # Remove the first occurrence
        if meal_plan.endswith("```"):
            meal_plan = meal_plan.rsplit("```", 1)[0]  # Remove the trailing part
 
        meal_plan_json = json.loads(meal_plan)
 
        st.title("Meal Plan")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Range")
            st.write(meal_plan_json["range"])
            st.subheader("Target")
            st.write(meal_plan_json["target"])
        with col2:
            st.subheader("BMI")
            st.write(meal_plan_json["bmi"])
            st.subheader("Days")
            st.write(meal_plan_json["total_days"])
 
        with col3:
            st.subheader(f"{aim}")
            st.write(meal_plan_json["difference"])
            st.subheader("Per week")
            st.write(meal_plan_json["weight_per_week"])
 
        st.subheader("Meal plan for 7 days")
        st.write(meal_plan_json["meal_plan"])