# 🩺 AI Medical Imaging AI Agent
<img width="1802" height="902" alt="image" src="https://github.com/user-attachments/assets/8a36767f-5d08-4f0c-8b9c-9148c497089c" />

## 🚀 Overview
• Built an Agentic AI–based medical imaging system to analyse X-ray, MRI, CT scan, and ultrasound images for AI-assisted diagnosis support
• Designed a multi-agent architecture with Medical Imaging Analysis Agent, Diagnostic Reasoning Agent, and Healthcare Coordinator Agent to autonomously process and interpret scans
• Leveraged Gemini Flash LLM to generate contextual diagnostic insights and explanations from imaging outputs
• Implemented Agentic AI design patterns (Tool Use, ReAct, Planning) to enable autonomous decision-making and reasoning across medical workflows
• Integrated AI medical imaging pipelines to detect anomalies and highlight potential issues that may be overlooked in manual review
• Enabled AI-assisted clinical Q&A, allowing doctors to ask questions about scans and receive explainable responses
• Developed a smart AI healthcare assistant to support doctors with faster image interpretation and patient diagnosis insights
• Architected the system to be modular, extensible, and cloud-ready, supporting hospital-scale deployment and future imaging modalities



```bash
#UV installation in windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version

#Virtual environment
uv venv multimodal --python 3.12
#installation of  
uv pip install -r requirements.txt
#Run app
streamlit run app.py --server.port=[PORT_NUMBER]



#Fast API
pip install "fastapi[standard]" uvicorn

#To run fast api 
uvicorn main:app --port 8080 --reload

#Fast api swagger
 http://127.0.0.1:8000/docs -> swagger api
```
