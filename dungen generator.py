import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import datetime

@st.cache_resource
def load_model(model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

# Streamlit UI
st.title(" AI Dungeon Story Generator")
st.markdown("Generate interactive stories using GPT-2/GPT-Neo.")

genre = st.selectbox("Choose a Genre", ["Fantasy", "Mystery", "Sci-Fi", "Adventure", "Horror", "Moral"])
prompt = st.text_area("Enter your story prompt:", "Once upon a time in a distant kingdom...")
max_length = st.slider("Max Length of Story", 50, 500, 150)

generate_btn = st.button("Generate Story")

if generate_btn and prompt:
    tokenizer, model = load_model("gpt2")
    input_ids = tokenizer.encode(f"{genre} Story: {prompt}", return_tensors="pt")

    with st.spinner("Generating story..."):
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=3,
            no_repeat_ngram_size=2,
            temperature=0.9,
            top_p=0.95,
            do_sample=True
        )

    st.subheader("Story Continuations:")
    for i, story in enumerate(output):
        text = tokenizer.decode(story, skip_special_tokens=True)
        st.markdown(f"**Option {i+1}:**")
        st.markdown(text.replace("\n", " "))

    if st.button(" Save Story"):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"story_{now}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        st.success("Story saved!")

