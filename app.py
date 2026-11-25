import streamlit as st

st.set_page_config(page_title="AI-Powered Requirements Analyzer", layout="wide")

st.title("AI-Powered Requirements Analyzer")
st.write("Convert messy stakeholder notes into clean BRD, Requirements, User Stories & Conflicts.")

st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password", help="Get free key from console.groq.com")
st.sidebar.write("Model: openai/gpt-oss-120b (Locked)")

st.subheader("1. Input Messy Requirements")

sample_data = """MEETING NOTES:
Dr. Mehta said 10-12 patients out of 40-50 do not show up daily. Ramesh said 2 patients were given same slot once.
EMAIL FROM ADMIN:
Patient should book online. Payment UPI and Card both. Reminder 1 day before and same day morning.
WHATSAPP CHAT:
Patient paid but booking not confirmed, money deducted. Keep 2 slots reserved for emergency.
CALL TRANSCRIPT:
Normal patient 10 min, new patient 15-20 min. Cancellation up to 2 hours before full refund, after that unclear.
"""

if st.button("Load Hospital Sample Data"):
    st.session_state["messy_input"] = sample_data

messy_input = st.text_area(
    "Paste messy notes here (Meeting / Email / WhatsApp / Call)",
    value=st.session_state.get("messy_input", ""),
    height=250
)

if st.button("Analyze Requirements"):
    if not api_key:
        st.error("Please enter Groq API Key in sidebar.")
    elif not messy_input:
        st.error("Please paste requirements or load sample data.")
    else:
        st.info("Part 1 working! In Part 2, we will connect AI here.")
        st.write("Your input length:", len(messy_input), "characters")
