# # # import streamlit as st
# # # import fitz  # PyMuPDF
# # # import google.generativeai as genai
# # # import io
# # # import os
# # # from PIL import Image
# # # from dotenv import load_dotenv

# # # # Load API Key
# # # load_dotenv()
# # # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # # if not GEMINI_API_KEY:
# # #     st.error("❌ Gemini API Key not found! Add it to your .env file.")
# # #     st.stop()

# # # # Configure Google Gemini API
# # # genai.configure(api_key=GEMINI_API_KEY)

# # # def extract_text_from_pdf(pdf_bytes):
# # #     """Extracts text from a PDF file."""
# # #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# # #     text = "\n".join(page.get_text("text") for page in doc)
# # #     return text

# # # def extract_images_from_pdf(pdf_bytes):
# # #     """Extracts images from a PDF file."""
# # #     images = []
# # #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# # #     for page in doc:
# # #         for img in page.get_images(full=True):
# # #             xref = img[0]
# # #             base_image = doc.extract_image(xref)
# # #             image_bytes = base_image["image"]
# # #             image = Image.open(io.BytesIO(image_bytes))
# # #             images.append(image)
# # #     return images

# # # def generate_response(prompt, pdf_text, history):
# # #     """Generates a response using Gemini AI with correct input formatting."""
# # #     try:
# # #         model = genai.GenerativeModel("gemini-2.0-flash")

# # #         # Build the conversation context
# # #         conversation = "\n".join(history) + f"\nUser: {prompt}\n\nPDF Content: {pdf_text}"

# # #         # Create a structured input format
# # #         response = model.generate_content([{"text": conversation}])

# # #         return response.text  # Extract the response text
# # #     except Exception as e:
# # #         return f"❌ Error: {str(e)}"



# # # # Custom CSS for a modern UI
# # # st.markdown("""
# # #     <style>
# # #         body { background-color: #f5f7fa; }
# # #         .stApp { max-width: 1000px; margin: auto; }
# # #         .title { text-align: center; font-size: 36px; color: #4A90E2; }
# # #         .sidebar .sidebar-content { background: linear-gradient(to bottom, #4A90E2, #0056b3); color: white; }
# # #         .chat-container { background: #f9f9f9; padding: 15px; border-radius: 10px; margin-top: 10px; }
# # #         .chat-user { background: #007bff; color: white; padding: 10px; border-radius: 8px; }
# # #         .chat-bot { background: #e9ecef; padding: 10px; border-radius: 8px; }
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # Streamlit Sidebar for Navigation
# # # st.sidebar.title("📌 Navigation")
# # # page = st.sidebar.radio("Go to:", ["🔍 Upload PDF", "💬 Chat with PDF"])

# # # # Streamlit App UI
# # # st.title("📄 Chat with Your PDF (Gemini AI)")

# # # if page == "🔍 Upload PDF":
# # #     st.subheader("📂 Upload a PDF")
# # #     uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# # #     if uploaded_file:
# # #         pdf_bytes = uploaded_file.read()
# # #         with st.spinner("🔍 Extracting data..."):
# # #             extracted_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
# # #             images = extract_images_from_pdf(io.BytesIO(pdf_bytes))

# # #             # Store the extracted text in session state
# # #             st.session_state.pdf_text = extracted_text

# # #             # Display extracted text
# # #             st.subheader("📜 Extracted Text")
# # #             st.text_area("PDF Text", extracted_text, height=300)

# # #             # Display extracted images
# # #             if images:
# # #                 st.subheader("🖼️ Extracted Images")
# # #                 for img in images:
# # #                     st.image(img, caption="Extracted Image", use_column_width=True)

# # # elif page == "💬 Chat with PDF":
# # #     st.subheader("💬 AI Chat with Your PDF")

# # #     # Ensure extracted text is available
# # #     if "pdf_text" not in st.session_state or not st.session_state.pdf_text:
# # #         st.warning("⚠️ Please upload a PDF first.")
# # #     else:
# # #         if "chat_history" not in st.session_state:
# # #             st.session_state.chat_history = []  # Initialize chat history

# # #         user_prompt = st.text_input("Ask something about the PDF:")

# # #         if user_prompt:
# # #             with st.spinner("🤖 AI is thinking..."):
# # #                 response = generate_response(user_prompt, st.session_state.pdf_text, st.session_state.chat_history)

# # #             # Store conversation history
# # #             st.session_state.chat_history.append(f"User: {user_prompt}")
# # #             st.session_state.chat_history.append(f"Bot: {response}")

# # #             # Display chat history
# # #             st.subheader("🧠 AI Conversation")
# # #             for i in range(0, len(st.session_state.chat_history), 2):
# # #                 user_msg = st.session_state.chat_history[i]
# # #                 bot_msg = st.session_state.chat_history[i + 1] if i + 1 < len(st.session_state.chat_history) else ""

# # #                 st.markdown(f'<div class="chat-container"><div class="chat-user">{user_msg}</div></div>', unsafe_allow_html=True)
# # #                 st.markdown(f'<div class="chat-container"><div class="chat-bot">{bot_msg}</div></div>', unsafe_allow_html=True)
# # import streamlit as st
# # import fitz  # PyMuPDF
# # import google.generativeai as genai
# # import io
# # import os
# # from PIL import Image
# # from dotenv import load_dotenv
# # import base64

# # # Load API Key
# # load_dotenv()
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # if not GEMINI_API_KEY:
# #     st.error("❌ Gemini API Key not found! Add it to your .env file.")
# #     st.stop()

# # # Configure Google Gemini API
# # genai.configure(api_key=GEMINI_API_KEY)

# # def extract_text_from_pdf(pdf_bytes):
# #     """Extracts text from a PDF file."""
# #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# #     text = "\n".join(page.get_text("text") for page in doc)
# #     return text

# # def extract_images_from_pdf(pdf_bytes):
# #     """Extracts images from a PDF file."""
# #     images = []
# #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# #     for page in doc:
# #         for img in page.get_images(full=True):
# #             xref = img[0]
# #             base_image = doc.extract_image(xref)
# #             image_bytes = base_image["image"]
# #             image = Image.open(io.BytesIO(image_bytes))
# #             images.append(image)
# #     return images

# # def generate_response(prompt, pdf_text, history):
# #     """Generates a response using Gemini AI with correct input formatting."""
# #     try:
# #         model = genai.GenerativeModel("gemini-2.0-flash")

# #         # Build the conversation context
# #         conversation = "\n".join(history) + f"\nUser: {prompt}\n\nPDF Content: {pdf_text}"

# #         # Create a structured input format
# #         response = model.generate_content([{"text": conversation}])

# #         return response.text  # Extract the response text
# #     except Exception as e:
# #         return f"❌ Error: {str(e)}"

# # def display_pdf(pdf_bytes):
# #     """Displays a PDF in the Streamlit app using base64 encoding without toolbar."""
# #     base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
# #     # Add #toolbar=0 to hide the PDF toolbar
# #     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="700" height="500" type="application/pdf" style="border: none;"></iframe>'
# #     st.markdown(pdf_display, unsafe_allow_html=True)

# # # Custom CSS for a modern UI
# # st.markdown("""
# #     <style>
# #         body { background-color: #f5f7fa; }
# #         .stApp { max-width: 1000px; margin: auto; }
# #         .title { text-align: center; font-size: 36px; color: #4A90E2; }
# #         .sidebar .sidebar-content { background: linear-gradient(to bottom, #4A90E2, #0056b3); color: white; }
# #         .chat-container { background: #f9f9f9; padding: 15px; border-radius: 10px; margin-top: 10px; }
# #         .chat-user { background: #007bff; color: white; padding: 10px; border-radius: 8px; }
# #         .chat-bot { background: #e9ecef; padding: 10px; border-radius: 8px; }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Streamlit Sidebar for Navigation
# # st.sidebar.title("📌 Navigation")
# # page = st.sidebar.radio("Go to:", ["🔍 Upload PDF"])  # Removed "Chat with PDF" option

# # # Streamlit App UI
# # st.title("📄 Chat with Your PDF (Gemini AI)")

# # if page == "🔍 Upload PDF":
# #     st.subheader("📂 Upload a PDF")
# #     uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# #     if uploaded_file:
# #         pdf_bytes = uploaded_file.read()
# #         with st.spinner("🔍 Extracting data..."):
# #             # Display the uploaded PDF without toolbar
# #             st.subheader("📜 Uploaded PDF")
# #             display_pdf(pdf_bytes)

# #             # Extract text (but don't display it)
# #             extracted_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
# #             # Extract images (but don't display them)
# #             images = extract_images_from_pdf(io.BytesIO(pdf_bytes))

# #             # Store the extracted text in session state
# #             st.session_state.pdf_text = extracted_text

# #         # Add chat functionality below the PDF viewer
# #         if "pdf_text" in st.session_state and st.session_state.pdf_text:
# #             if "chat_history" not in st.session_state:
# #                 st.session_state.chat_history = []  # Initialize chat history

# #             # Prompt input field below the PDF viewer
# #             st.subheader("💬 Ask a Question About the PDF")
# #             user_prompt = st.text_input("Enter your question here:")

# #             if user_prompt:
# #                 with st.spinner("🤖 AI is thinking..."):
# #                     response = generate_response(user_prompt, st.session_state.pdf_text, st.session_state.chat_history)

# #                 # Store conversation history
# #                 st.session_state.chat_history.append(f"User: {user_prompt}")
# #                 st.session_state.chat_history.append(f"Bot: {response}")

# #                 # Display chat history below the prompt
# #                 st.subheader("🧠 AI Conversation")
# #                 for i in range(0, len(st.session_state.chat_history), 2):
# #                     user_msg = st.session_state.chat_history[i]
# #                     bot_msg = st.session_state.chat_history[i + 1] if i + 1 < len(st.session_state.chat_history) else ""

# #                     st.markdown(f'<div class="chat-container"><div class="chat-user">{user_msg}</div></div>', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="chat-container"><div class="chat-bot">{bot_msg}</div></div>', unsafe_allow_html=True)
# # import streamlit as st
# # import fitz  # PyMuPDF
# # import google.generativeai as genai
# # import io
# # import os
# # from PIL import Image
# # from dotenv import load_dotenv
# # import base64
# # import speech_recognition as sr

# # # Load API Key
# # load_dotenv()
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # if not GEMINI_API_KEY:
# #     st.error("❌ Gemini API Key not found! Add it to your .env file.")
# #     st.stop()

# # # Configure Google Gemini API
# # genai.configure(api_key=GEMINI_API_KEY)

# # def extract_text_from_pdf(pdf_bytes):
# #     """Extracts text from a PDF file."""
# #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# #     text = "\n".join(page.get_text("text") for page in doc)
# #     return text

# # def extract_images_from_pdf(pdf_bytes):
# #     """Extracts images from a PDF file."""
# #     images = []
# #     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
# #     for page in doc:
# #         for img in page.get_images(full=True):
# #             xref = img[0]
# #             base_image = doc.extract_image(xref)
# #             image_bytes = base_image["image"]
# #             image = Image.open(io.BytesIO(image_bytes))
# #             images.append(image)
# #     return images

# # def generate_response(prompt, pdf_text, history):
# #     """Generates a response using Gemini AI with correct input formatting."""
# #     try:
# #         model = genai.GenerativeModel("gemini-2.0-flash")

# #         # Build the conversation context
# #         conversation = "\n".join(history) + f"\nUser: {prompt}\n\nPDF Content: {pdf_text}"

# #         # Create a structured input format
# #         response = model.generate_content([{"text": conversation}])

# #         return response.text  # Extract the response text
# #     except Exception as e:
# #         return f"❌ Error: {str(e)}"

# # def display_pdf(pdf_bytes):
# #     """Displays a PDF in the Streamlit app using base64 encoding without toolbar."""
# #     base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
# #     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="700" height="500" type="application/pdf" style="border: none;"></iframe>'
# #     st.markdown(pdf_display, unsafe_allow_html=True)

# # def speech_to_text():
# #     """Captures audio from the microphone and converts it to text."""
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         st.info("🎙️ Listening... Please speak your query.")
# #         recognizer.adjust_for_ambient_noise(source, duration=1)
# #         try:
# #             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
# #             st.info("🎙️ Processing your speech...")
# #             text = recognizer.recognize_google(audio)
# #             return text
# #         except sr.WaitTimeoutError:
# #             st.error("⏳ No speech detected within the timeout period.")
# #             return ""
# #         except sr.UnknownValueError:
# #             st.error("❓ Could not understand the audio.")
# #             return ""
# #         except sr.RequestError as e:
# #             st.error(f"❌ Speech recognition error: {e}")
# #             return ""

# # # Custom CSS (removed JavaScript since text-to-speech is no longer needed)
# # st.markdown("""
# #     <style>
# #         body { background-color: #f5f7fa; }
# #         .stApp { max-width: 1000px; margin: auto; }
# #         .title { text-align: center; font-size: 36px; color: #4A90E2; }
# #         .sidebar .sidebar-content { background: linear-gradient(to bottom, #4A90E2, #0056b3); color: white; }
# #         .chat-container { background: #f9f9f9; padding: 15px; border-radius: 10px; margin-top: 10px; }
# #         .chat-user { background: #007bff; color: white; padding: 10px; border-radius: 8px; }
# #         .chat-bot { background: #e9ecef; padding: 10px; border-radius: 8px; }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Streamlit Sidebar for Navigation
# # st.sidebar.title("📌 Navigation")
# # page = st.sidebar.radio("Go to:", ["🔍 Upload PDF"])

# # # Streamlit App UI
# # st.title("📄 Chat with Your PDF (Gemini AI)")

# # if page == "🔍 Upload PDF":
# #     st.subheader("📂 Upload a PDF")
# #     uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

# #     if uploaded_file:
# #         # Check if the uploaded file has changed
# #         if "previous_pdf" not in st.session_state:
# #             st.session_state.previous_pdf = None

# #         # Compute a unique identifier for the uploaded file (e.g., its name)
# #         current_pdf_id = uploaded_file.name
# #         if st.session_state.previous_pdf != current_pdf_id:
# #             # A new PDF has been uploaded; clear the chat history and other state
# #             st.session_state.chat_history = []
# #             st.session_state.user_prompt = ""
# #             st.session_state.prompt_input = ""
# #             st.session_state.pdf_text = None
# #             st.session_state.previous_pdf = current_pdf_id

# #         pdf_bytes = uploaded_file.read()
# #         with st.spinner("🔍 Extracting data..."):
# #             # Display the uploaded PDF without toolbar
# #             st.subheader("📜 Uploaded PDF")
# #             display_pdf(pdf_bytes)

# #             # Extract text (but don't display it)
# #             extracted_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
# #             # Extract images (but don't display them)
# #             images = extract_images_from_pdf(io.BytesIO(pdf_bytes))

# #             # Store the extracted text in session state
# #             st.session_state.pdf_text = extracted_text

# #         # Add chat functionality below the PDF viewer
# #         if "pdf_text" in st.session_state and st.session_state.pdf_text:
# #             if "chat_history" not in st.session_state:
# #                 st.session_state.chat_history = []  # Initialize chat history

# #             # Initialize session state for the prompt and prompt_input
# #             if "user_prompt" not in st.session_state:
# #                 st.session_state.user_prompt = ""
# #             if "prompt_input" not in st.session_state:
# #                 st.session_state.prompt_input = ""

# #             # Prompt input field with speech-to-text
# #             st.subheader("💬 Ask a Question About the PDF")
# #             st.info("Click the 'Start Listening' button to speak your query, or type it directly.")

# #             # Speech-to-text button
# #             st.subheader("🎙 Speak Your Query")
# #             if st.button("🎤 Start Listening"):
# #                 spoken_text = speech_to_text()
# #                 if spoken_text:
# #                     st.session_state.user_prompt = spoken_text
# #                     st.session_state.prompt_input = spoken_text
# #                     st.write("📝 You said:", spoken_text)

# #             # Input field for the prompt
# #             user_prompt = st.text_input("Enter your question here:", value=st.session_state.user_prompt, key="prompt-input", on_change=lambda: st.session_state.update(user_prompt=st.session_state["prompt-input"]))

# #             if st.session_state.user_prompt:
# #                 with st.spinner("🤖 AI is thinking..."):
# #                     response = generate_response(st.session_state.user_prompt, st.session_state.pdf_text, st.session_state.chat_history)

# #                 # Store conversation history (latest entry will be appended at the end)
# #                 st.session_state.chat_history.append(f"User: {st.session_state.user_prompt}")
# #                 st.session_state.chat_history.append(f"Bot: {response}")

# #                 # Clear the prompt input after submission
# #                 st.session_state.user_prompt = ""
# #                 st.session_state.prompt_input = ""

# #             # Display chat history in reverse chronological order (latest first)
# #             st.subheader("🧠 AI Conversation")
# #             if st.session_state.chat_history:
# #                 # Reverse the chat history to show the latest conversation first
# #                 reversed_history = st.session_state.chat_history[::-1]
# #                 for i in range(0, len(reversed_history), 2):
# #                     bot_msg = reversed_history[i] if i < len(reversed_history) else ""  # Bot message comes first in reversed order
# #                     user_msg = reversed_history[i + 1] if i + 1 < len(reversed_history) else ""  # User message comes second
# #                     st.markdown(f'<div class="chat-container"><div class="chat-user">{user_msg}</div></div>', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="chat-container"><div class="chat-bot">{bot_msg}</div></div>', unsafe_allow_html=True)
# #             else:
# #                 st.write("No conversation yet. Ask a question to start!")   
# import streamlit as st
# import fitz  # PyMuPDF
# import google.generativeai as genai
# import io
# import os
# from PIL import Image
# from dotenv import load_dotenv
# import base64
# import speech_recognition as sr

# # Load API Key
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     st.error("❌ Gemini API Key not found! Add it to your .env file.")
#     st.stop()

# # Configure Google Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Custom CSS for Sky-Blue Theme
# st.markdown("""
#     <style>
#     body {
#         background-color: #e0f2fe;
#         font-family: 'Arial', sans-serif;
#     }
#     .stApp {
#         background-color: #e0f2fe;
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     h1, h2, h3 {
#         color: #0369a1;
#         text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
#     }
#     .stButton>button {
#         background-color: #0284c7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-weight: bold;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #0369a1;
#     }
#     .stTextInput>input, .stTextArea>textarea {
#         border: 2px solid #7dd3fc;
#         border-radius: 8px;
#         background-color: #f0f9ff;
#         color: #0c4a6e;
#     }
#     .stRadio>label, .stSidebar {
#         background-color: #f0f9ff;
#         border: 2px solid #7dd3fc;
#         border-radius: 8px;
#         padding: 5px;
#     }
#     .stFileUploader {
#         background-color: #f0f9ff;
#         border: 2px dashed #7dd3fc;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     .stSuccess, .stWarning, .stError, .stInfo {
#         background-color: #bae6fd;
#         border: 1px solid #7dd3fc;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     .chat-user {
#         background: #0284c7;
#         color: white;
#         padding: 10px;
#         border-radius: 8px;
#         margin: 5px 0;
#     }
#     .chat-bot {
#         background: #e0f2fe;
#         color: #0c4a6e;
#         padding: 10px;
#         border-radius: 8px;
#         margin: 5px 0;
#     }
#     .chat-container {
#         background: #f0f9ff;
#         padding: 15px;
#         border-radius: 10px;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# def extract_text_from_pdf(pdf_bytes):
#     """Extracts text from a PDF file."""
#     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
#     text = "\n".join(page.get_text("text") for page in doc)
#     return text

# def extract_images_from_pdf(pdf_bytes):
#     """Extracts images from a PDF file."""
#     images = []
#     doc = fitz.open(stream=pdf_bytes, filetype="pdf")
#     for page in doc:
#         for img in page.get_images(full=True):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#             image_bytes = base_image["image"]
#             image = Image.open(io.BytesIO(image_bytes))
#             images.append(image)
#     return images

# def generate_response(prompt, pdf_text, history):
#     """Generates a response using Gemini AI with correct input formatting."""
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")  # Update to correct model if needed
#         conversation = "\n".join(history) + f"\nUser: {prompt}\n\nPDF Content: {pdf_text}"
#         response = model.generate_content([{"text": conversation}])
#         return response.text
#     except Exception as e:
#         return f"❌ Error: {str(e)}"

# def display_pdf(pdf_bytes):
#     """Displays a PDF in the Streamlit app using base64 encoding without toolbar."""
#     base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="700" height="500" type="application/pdf" style="border: none;"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

# def speech_to_text():
#     """Captures audio from the microphone and converts it to text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎙️ Listening... Please speak your query.")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             st.info("🎙️ Processing your speech...")
#             text = recognizer.recognize_google(audio)
#             return text
#         except sr.WaitTimeoutError:
#             st.error("⏳ No speech detected within the timeout period.")
#             return ""
#         except sr.UnknownValueError:
#             st.error("❓ Could not understand the audio.")
#             return ""
#         except sr.RequestError as e:
#             st.error(f"❌ Speech recognition error: {e}")
#             return ""

# # Streamlit Sidebar for Navigation
# st.sidebar.title("📌 Navigation")
# page = st.sidebar.radio("Go to:", ["🔍 Upload PDF"])

# # Streamlit App UI
# st.title("📄 Chat with Your PDF (Gemini AI)")
# st.write("✨ Upload a PDF (up to 1 GB) and ask questions about its content!")

# if page == "🔍 Upload PDF":
#     st.subheader("📂 Upload a PDF")
#     uploaded_file = st.file_uploader(
#         "Drag and drop file here - Limit 1 GB per file • PDF",
#         type=["pdf"]
#     )

#     if uploaded_file:
#         # Check if the uploaded file has changed
#         if "previous_pdf" not in st.session_state:
#             st.session_state.previous_pdf = None

#         current_pdf_id = uploaded_file.name
#         if st.session_state.previous_pdf != current_pdf_id:
#             st.session_state.chat_history = []
#             st.session_state.user_prompt = ""
#             st.session_state.prompt_input = ""
#             st.session_state.pdf_text = None
#             st.session_state.previous_pdf = current_pdf_id

#         pdf_bytes = uploaded_file.read()
#         with st.spinner("🔍 Extracting data..."):
#             st.subheader("📜 Uploaded PDF")
#             display_pdf(pdf_bytes)
#             extracted_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
#             images = extract_images_from_pdf(io.BytesIO(pdf_bytes))
#             st.session_state.pdf_text = extracted_text

#         # Chat functionality
#         if "pdf_text" in st.session_state and st.session_state.pdf_text:
#             if "chat_history" not in st.session_state:
#                 st.session_state.chat_history = []

#             if "user_prompt" not in st.session_state:
#                 st.session_state.user_prompt = ""
#             if "prompt_input" not in st.session_state:
#                 st.session_state.prompt_input = ""

#             st.subheader("💬 Ask a Question About the PDF")
#             st.info("Click 'Start Listening' to speak your query, or type it directly.")

#             if st.button("🎤 Start Listening"):
#                 spoken_text = speech_to_text()
#                 if spoken_text:
#                     st.session_state.user_prompt = spoken_text
#                     st.session_state.prompt_input = spoken_text
#                     st.write("📝 You said:", spoken_text)

#             user_prompt = st.text_input(
#                 "Enter your question here:",
#                 value=st.session_state.user_prompt,
#                 key="prompt-input",
#                 placeholder="e.g., What is the main topic of this PDF?",
#                 on_change=lambda: st.session_state.update(user_prompt=st.session_state["prompt-input"])
#             )

#             if st.session_state.user_prompt:
#                 with st.spinner("🤖 AI is thinking..."):
#                     response = generate_response(st.session_state.user_prompt, st.session_state.pdf_text, st.session_state.chat_history)
#                 st.session_state.chat_history.append(f"User: {st.session_state.user_prompt}")
#                 st.session_state.chat_history.append(f"Bot: {response}")
#                 st.session_state.user_prompt = ""
#                 st.session_state.prompt_input = ""

#             st.subheader("🧠 AI Conversation")
#             if st.session_state.chat_history:
#                 reversed_history = st.session_state.chat_history[::-1]
#                 for i in range(0, len(reversed_history), 2):
#                     bot_msg = reversed_history[i] if i < len(reversed_history) else ""
#                     user_msg = reversed_history[i + 1] if i + 1 < len(reversed_history) else ""
#                     st.markdown(f'<div class="chat-container"><div class="chat-user">{user_msg}</div></div>', unsafe_allow_html=True)
#                     st.markdown(f'<div class="chat-container"><div class="chat-bot">{bot_msg}</div></div>', unsafe_allow_html=True)
#             else:
#                 st.write("No conversation yet. Ask a question to start!")

# st.success("✅ Ready! Upload a PDF (up to 1 GB) and start chatting!")
import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai
import io
import os
from PIL import Image
from dotenv import load_dotenv
import base64
import speech_recognition as sr

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ Gemini API Key not found! Add it to your .env file.")
    st.stop()

# Configure Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Custom CSS for Sky-Blue Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #e0f2fe;
    }
    h1, h2, h3 {
        color: #0369a1;
    }
    .stButton>button {
        background-color: #0284c7;
        color: white;
    }
    .chat-container {
        background: #f0f9ff;
        padding: 15px;
        border-radius: 10px;
    }
    .chat-user {
        background: #0284c7;
        color: white;
        padding: 10px;
        border-radius: 8px;
    }
    .chat-bot {
        background: #e0f2fe;
        color: #0c4a6e;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    return "\n".join(page.get_text("text") for page in doc)

def generate_response(prompt, pdf_text, history):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        conversation = "\n".join(history) + f"\nUser: {prompt}\n\nPDF Content: {pdf_text}"
        response = model.generate_content([{"text": conversation}])
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def display_pdf(pdf_bytes):
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="700" height="500"></iframe>', unsafe_allow_html=True)



st.sidebar.title("📌 Navigation")
st.sidebar.radio("Go to:", ["🔍 Upload PDF"])

st.title("📄 Chat with Your PDF (Gemini AI)")
st.write("✨ Upload a PDF and ask questions!")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_bytes = uploaded_file.read()
    display_pdf(pdf_bytes)
    pdf_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.subheader("💬 Ask a Question")
    

    
    user_prompt = st.text_input("Enter your question:", "", key="prompt-input")
    
    if user_prompt:
        response = generate_response(user_prompt, pdf_text, st.session_state.chat_history)
        st.session_state.chat_history.append(f"User: {user_prompt}")
        st.session_state.chat_history.append(f"Bot: {response}")
    
    st.subheader("🧠 AI Conversation")
    for i in reversed(range(0, len(st.session_state.chat_history), 2)):
        user_msg = st.session_state.chat_history[i]
        bot_msg = st.session_state.chat_history[i + 1] if i + 1 < len(st.session_state.chat_history) else ""
        st.markdown(f'<div class="chat-container"><div class="chat-user">{user_msg}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-container"><div class="chat-bot">{bot_msg}</div></div>', unsafe_allow_html=True)

st.success("✅ Ready! Upload a PDF and start chatting!")
