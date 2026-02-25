import streamlit as st
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="🏋️‍♂️",
    layout="wide"
)

# ================= HEADER =================
st.markdown(
    """
    <h1 style="text-align:center;">🏋️‍♂️ AI Personalized Workout & Diet Planner</h1>
    <p style="text-align:center; font-size:18px;">
    Personalized plans generated directly from your inputs
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ================= SIDEBAR INPUT =================
st.sidebar.header("📥 Input Your Details")

age = st.sidebar.slider("Age", 15, 60, 21)
height = st.sidebar.slider("Height (cm)", 140, 210, 170)
weight = st.sidebar.slider("Weight (kg)", 40, 150, 65)

st.sidebar.subheader("🎯 Preferences")

goal = st.sidebar.radio(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Stay Fit"]
)

diet_type = st.sidebar.radio(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian"]
)

budget = st.sidebar.selectbox(
    "Monthly Food Budget",
    ["Low", "Medium", "High"]
)

workout_place = st.sidebar.radio(
    "Workout Place",
    ["Home", "Gym"]
)

st.sidebar.divider()
generate = st.sidebar.button("🚀 Generate Plan", use_container_width=True)

# ================= MAIN CONTENT =================
if not generate:
    st.markdown(
        """
        ### 👋 Welcome!
        This system generates a *fitness & diet plan strictly based on the data you provide*.

        #### 🔍 Inputs considered:
        - Body metrics (BMI)
        - Fitness goal
        - Diet preference
        - Budget constraints
        - Workout availability

        👉 Enter details on the *left sidebar* and click  
        *“Generate Plan”*
        """
    )

else:
    payload = {
        "age": age,
        "height": height,
        "weight": weight,
        "goal": goal,
        "diet_type": diet_type,
        "budget": budget,
        "workout_place": workout_place
    }

    with st.spinner("🧠 Generating plan based on your data..."):
        response = requests.post(
            "http://127.0.0.1:8000/generate-plan",
            json=payload
        )

    if response.status_code == 200:
        result = response.json()

        # ================= INPUT SUMMARY =================
        st.success("✅ Plan Generated Successfully")

        st.markdown("## 📌 Your Provided Data (Input Summary)")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Age", age)
        col2.metric("Height (cm)", height)
        col3.metric("Weight (kg)", weight)
        col4.metric("BMI", result["BMI"])

        colA, colB, colC, colD = st.columns(4)
        colA.info(f"🎯 Goal: {goal}")
        colB.info(f"🥗 Diet: {diet_type}")
        colC.info(f"💰 Budget: {budget}")
        colD.info(f"🏠 Workout: {workout_place}")

        st.divider()

        # ================= OUTPUT =================
        st.markdown("## 🏋️ Personalized Workout Plan")
        st.write(
            f"""
            **Based on your goal: {goal}  
            Workout location: {workout_place}**

            {result["Workout Plan"]}
            """
        )

        st.divider()

        st.markdown("## 🥗 Personalized Diet Plan")
        st.write(
            f"""
            **Based on your diet preference: {diet_type}  
            Budget level: {budget}**

            {result["Diet Plan"]}
            """
        )

        st.divider()

        # ================= EXPLANATION =================
        st.markdown(
            """
            ## 🤖 How This Plan Was Generated
            - BMI calculated using your height & weight
            - Workout chosen based on fitness goal and location
            - Diet selected based on food preference and budget
            - Plan optimized for a student lifestyle

            ✔ Transparent  
            ✔ Explainable  
            ✔ Personalized  
            """
        )

    else:
        st.error("❌ Backend error. Please ensure FastAPI server is running.")

# ================= FOOTER =================
st.divider()
st.markdown(
    "<p style='text-align:center; font-size:13px;'>🚀 AI Fitness Planner • Data-Driven Hackathon Project</p>",
    unsafe_allow_html=True
)