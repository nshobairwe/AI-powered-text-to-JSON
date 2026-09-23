import requests
import streamlit as st


# ==================================================
# Configuration
# ==================================================

API_URL = "http://127.0.0.1:8000/extract"


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="AI Text-to-JSON Extractor",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# Header
# ==================================================

st.title("🤖 AI Text-to-JSON Extractor")

st.caption(
    "Extract structured information from natural-language text "
    "using Llama 3.2 + Ollama + JSON Schema."
)


# ==================================================
# Create Two Columns
# ==================================================

left, right = st.columns(
    [1, 1],
    gap="large"
)


# ==================================================
# LEFT SIDE — INPUT
# ==================================================

with left:

    st.subheader("📝 Input Text")

    user_text = st.text_area(
        "Enter your text",
        height=350,
        placeholder=(
            "Example:\n\n"
            "My name is Witness. I am 25 years old and "
            "I live in Dar es Salaam. I am a Software "
            "Developer with skills in Python, Django and "
            "FastAPI. I am looking for a Python backend job."
        ),
        label_visibility="collapsed"
    )

    extract_button = st.button(
        "🚀 Extract Information",
        use_container_width=True
    )


# ==================================================
# RIGHT SIDE — RESULT
# ==================================================

with right:

    st.subheader("📦 Structured JSON")

    if extract_button:

        if not user_text.strip():

            st.warning(
                "Please enter some text first."
            )

        else:

            with st.spinner(
                "Llama 3.2 is extracting information..."
            ):

                try:

                    response = requests.post(
                        API_URL,
                        json={
                            "text": user_text
                        },
                        timeout=120
                    )

                    # ----------------------------------
                    # Successful Response
                    # ----------------------------------

                    if response.status_code == 200:

                        result = response.json()

                        st.success(
                            "Information extracted successfully!"
                        )

                        # Show JSON
                        st.json(result)

                        # ----------------------------------
                        # Extracted Fields
                        # ----------------------------------

                        st.subheader(
                            "📋 Extracted Information"
                        )

                        col1, col2 = st.columns(2)

                        with col1:

                            st.write(
                                "**Name**"
                            )
                            st.write(
                                result.get("name")
                            )

                            st.write(
                                "**Age**"
                            )
                            st.write(
                                result.get("age")
                            )

                            st.write(
                                "**Location**"
                            )
                            st.write(
                                result.get("location")
                            )

                            st.write(
                                "**Profession**"
                            )
                            st.write(
                                result.get("profession")
                            )

                        with col2:

                            st.write(
                                "**Skills**"
                            )

                            skills = result.get(
                                "skills", []
                            )

                            st.write(
                                ", ".join(skills)
                                if skills
                                else "Not provided"
                            )

                            st.write(
                                "**Email**"
                            )
                            st.write(
                                result.get("email")
                                or "Not provided"
                            )

                            st.write(
                                "**Job Interest**"
                            )
                            st.write(
                                result.get("job_interest")
                                or "Not provided"
                            )

                    # ----------------------------------
                    # API Error
                    # ----------------------------------

                    else:

                        st.error(
                            f"Backend Error: "
                            f"{response.text}"
                        )

                # --------------------------------------
                # Connection Error
                # --------------------------------------

                except requests.exceptions.ConnectionError:

                    st.error(
                        """
                        ❌ Could not connect to FastAPI.

                        Make sure the backend is running:

                        `uvicorn backend.main:app --reload`
                        """
                    )

                # --------------------------------------
                # Timeout
                # --------------------------------------

                except requests.exceptions.Timeout:

                    st.error(
                        "⏱️ The AI request timed out."
                    )

                # --------------------------------------
                # Other Errors
                # --------------------------------------

                except Exception as e:

                    st.error(
                        f"Unexpected error: {str(e)}"
                    )

    else:

        st.info(
            "👈 Enter text on the left and click "
            "'Extract Information' to see the structured "
            "JSON result here."
        )