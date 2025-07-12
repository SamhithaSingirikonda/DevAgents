# 🌐 DevAgents: Communicative Agents for Software Development

## 📖 Overview
**DevAgents** is a multi-agent AI system that simulates a virtual software company. In this company, intelligent agents work together to build complete software systems from a single-line user prompt. These agents take on specific roles such as:
- Chief Executive Officer (CEO)
- Chief Technology Officer (CTO)
- Chief Product Officer (CPO)
- Programmer
- Reviewer
- Tester
- Designer

Each agent is designed to act autonomously and collaboratively, enabling the automation of different phases of the software development lifecycle including:
- **Requirement gathering**
- **Planning and architecture design**
- **Coding**
- **Testing and review**
- **Documentation and final delivery**

This system uses large language models (LLMs) such as DeepSeek, GPT-4, and others via OpenRouter to interpret tasks, generate code, and reason across complex workflows.

Key Features:
- ✨ **No coding required to initiate**: Just describe your software idea in natural language.
- ⚖️ **Customizable agent roles and workflows**
- 🧐 **Research-ready platform** for multi-agent communication and collective intelligence studies
- ✨ **Supports OpenRouter for API access**, making it cost-effective with flexible LLM usage.

---

## ⚡ Quickstart (Terminal Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/SamhithaSingirikonda/DevAgents.git
cd DevAgents
```

### 2. Set Up Python Environment
Ensure Python 3.9+ is installed.
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File
Create a `.env` file in the root folder with the following:
```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL=deepseek-ai/deepseek-coder:6.7b
```

### 5. Build Your Software
Use a natural language description of your idea and a project name:
```bash
python run.py --task "build a 2048 game" --name "2048Game"
```

### 6. Run the Generated Software
```bash
cd WareHouse/2048Game_DefaultOrganization_timestamp
python main.py
```

---

## ✅ GitHub Best Practices for Teams

### .gitignore
Ensure the following entries are in your `.gitignore` to prevent pushing sensitive/unnecessary files:
```gitignore
.venv/
__pycache__/
.env
*.log
```

---

## 🔍 Example Prompt
```bash
python run.py --task "Build a basic login and register system" --name "LoginSystem"
```

---

Happy building with **DevAgents**! 💻🤖
