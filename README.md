AI Dungeon Story Generator

 Objective:

Create interactive, genre-based fantasy stories using generative AI (GPT-2 ) via a simple Streamlit interface.

Tools & Libraries Used:

- Python
- Streamlit
- Hugging Face Transformers
- Torch

 Features:

- Load pretrained GPT-2  from Hugging Face
- Enter custom story prompts
- Select genres like Fantasy, Mystery, Sci-Fi, Horror, etc.
- Generate 1 or more story continuations
- Save generated story to a .txt file
- Simple and responsive web interface (Streamlit)

 How to Run Locally:

1. Install requirements:
   pip install -r requirements.txt

2. Run the app:
   streamlit run dungen generator.py

 How to Deploy Online (Streamlit Cloud):

1. Push all files to a GitHub repository.
2. Go to https://streamlit.io/cloud
3. Click "New App" > Connect your GitHub > Choose the repo and `dungen generator.py`
4. Deploy!


 Author:

Bokketi Pranitha

