import streamlit as st
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
    BitsAndBytesConfig
)

from peft import PeftModel

st.set_page_config(
    page_title="Finance Chat Assistant",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Finance Chat Assistant")
st.write("Ask finance related questions")

def load_model():

    checkpoint = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    bnb = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        checkpoint,
        quantization_config=bnb,
        device_map="auto"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        "finance_chat_model"
    )

    model = PeftModel.from_pretrained(
        base_model,
        "finance_chat_model"
    )

    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer
    )

    return generator, tokenizer


generator, tokenizer = load_model()


examples = [
    "What is a mutual fund?",
    "How does diversification reduce risk?",
    "What is SIP investing?",
    "What is an ETF?",
    "How should a beginner start investing?",
    "What is asset allocation?",
    "How does inflation affect investments?"
]

selected_example = st.selectbox(
    "Try an example question",
    examples
)


question = st.text_input(
    "Ask a Finance Question",
    value=selected_example
)

if st.button("Generate"):

    if not question.strip():
        st.warning("Please enter a finance question.")

    else:

        messages = [
            {
                "role": "user",
                "content": question
            }
        ]

        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        with st.spinner("Generating answer..."):

            result = generator(
                prompt,
                max_new_tokens=120,
                repetition_penalty=1.2,
                do_sample=False,
                return_full_text=False
            )

        st.subheader("Answer")
        st.write(result[0]["generated_text"])