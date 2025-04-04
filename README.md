# 🧠 Agent Workflow System (Terminal-Based)

A modular terminal-based agent system capable of executing both simple and complex tasks using multiple agents and tools. Task results are saved automatically to the `Reports/` folder.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/VenerableHarsha/Multiagent-Core
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate the environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Before running the system, configure your API keys.

1. Navigate to the `config/` folder.
2. Create or edit `config.toml` with the following format:

```toml
[llm]
api_key = "your_llm_api_key"

[llm.vision]
api_key = "your_vision_model_api_key"
```

---

## 🧩 How It Works

The system is powered by:
- **Model Context Protocols** for shared knowledge across agents
- **Agents** for intelligent task segmentation and execution
- **Tools** for specific utility functions

The entire system is agent-driven, with multiple agents running concurrently. The **Core** agent acts as the controller and orchestrator.

The workflow follows this sequence:
- Prompt input from user
- Core agent initiates the plan
- Required agents and tools are selected based on the task
- Tools and agents gather the necessary information
- Execution of task using tools/agents
- Cleanup and termination

You can invoke the system via the terminal depending on the complexity of your task:

### ▶️ For Simple Tasks

```bash
python main.py
```

### 🧠 For Multi-Step Tasks

```bash
python flow_of_thoughts.py
```

> Input your task directly in the terminal when prompted.

---

## 📂 Reports

All outputs, results, and generated content will be automatically saved in the `Reports/` folder.

---

## 📀 Project Structure

This is the overall view of the important files.

```plaintext
├── main.py                # Entry point for simple tasks
├── flow_of_thoughts.py   # Entry point for multi-step tasks
├── config/
│   └── config.toml        # API key configuration
├── Reports/               # Stores generated reports
├── core/
│   ├── tools/             # Utility tools
│   ├── agents/            # Agent implementations
│   └── prompts/           # Prompt templates
├── requirements.txt       # Python dependencies
```

---

## ✅ Notes

- Make sure to activate your virtual environment before running any script.
- Ensure `config.toml` is properly set up with valid API keys.
- Supports both LLM and vision model tasks, including image inputs.
- Modular and extendable design for adding more agents or tools.

