# 💰 Finance Chat Assistant

A finance-focused conversational AI built by fine-tuning TinyLlama-1.1B-Chat using QLoRA and PEFT on the Bharti Finance Dataset.

The goal of this project is to create a lightweight finance assistant capable of answering questions related to investing, personal finance, mutual funds, SIPs, ETFs, risk management, and retirement planning.

---

## 🚀 Project Overview

This project demonstrates efficient fine-tuning of a Large Language Model (LLM) using:

* TinyLlama-1.1B-Chat-v1.0
* QLoRA (Quantized Low-Rank Adaptation)
* PEFT (Parameter-Efficient Fine-Tuning)
* Hugging Face Transformers
* TRL SFTTrainer
* BitsAndBytes 4-bit Quantization
* Streamlit Deployment

The resulting model is deployed as an interactive finance chatbot.

---

## 🎯 Features

* Finance-focused question answering
* Lightweight LoRA adapter training
* Streamlit web interface
* Hugging Face model deployment
* Efficient 4-bit quantized training
* Parameter-efficient fine-tuning
* Finance domain adaptation

---

## 🧠 Model Information

### Base Model

TinyLlama/TinyLlama-1.1B-Chat-v1.0

### Fine-Tuning Method

* QLoRA
* LoRA
* PEFT
* TRL SFTTrainer
* 4-bit NF4 Quantization

### Trainable Parameters

Only **0.1023%** of model parameters were trained.

This significantly reduces memory usage and training costs compared to full fine-tuning.

---

## 📊 Training Details

### Dataset

Bharti Finance Dataset

Topics covered:

* Personal Finance
* SIP Investing
* Mutual Funds
* ETFs
* Diversification
* Asset Allocation
* Inflation
* Risk Management
* Retirement Planning
* Investment Strategies

### Training Configuration

| Parameter            | Value                    |
| -------------------- | ------------------------ |
| Base Model           | TinyLlama-1.1B-Chat-v1.0 |
| Fine-Tuning          | QLoRA                    |
| Quantization         | 4-bit NF4                |
| Epochs               | 3                        |
| Trainable Parameters | 0.1023%                  |

---

## 📈 Results

### Validation Loss

| Epoch | Validation Loss |
| ----- | --------------- |
| 1     | 2.418959        |
| 2     | 2.409989        |
| 3     | 2.412288        |

### Best Validation Loss

**2.409989**

### Final Training Loss

**2.4259**

---

## 💻 Streamlit Application

The model is integrated into a Streamlit web application where users can ask finance-related questions and receive AI-generated responses.

Example topics:

* How does inflation affect investments?
* What is asset allocation?
* Explain SIP investing.
* How can diversification reduce risk?
* Compare mutual funds and ETFs.

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/kurannnnn/Finance-Chat-Assistant.git

cd Finance-Chat-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🤗 Hugging Face Model

Model Repository:

https://huggingface.co/Konnnnnnnn/finance-chat-assistant

---

## 📷 Screenshots

### Training Results

![Training Results](screenshots/training_results.png)

### Model Comparison

![Model Comparison](screenshots/model_comparison.png)

### Application Interface

![Application Interface](screenshots/app_home.png)

### Sample Response

![Sample Response](screenshots/app_response.png)

---

## ⚠️ Limitations

This model is intended for educational and research purposes only.

It should **not** be used for:

* Professional financial advice
* Tax advice
* Legal advice
* Real-money investment decisions
* Portfolio management without expert supervision

The model may generate inaccurate or outdated information and users should verify financial information from trusted sources.

---

## 🔮 Future Improvements

* Larger finance datasets
* Better evaluation benchmarks
* RAG integration
* Human preference evaluation
* Improved factual accuracy
* Hugging Face Spaces deployment

---

## 🛠 Technologies Used

* Python
* PyTorch
* Transformers
* PEFT
* TRL
* BitsAndBytes
* Streamlit
* QLoRA
* TinyLlama

---

## 👤 Author

Kuran

---

## 📜 License

MIT License
