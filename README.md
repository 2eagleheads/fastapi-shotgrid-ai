
---

> ⚠️ **Project Status: In Active Development**
> This project is still under construction — features may change and bugs are possible. Use with caution and feel free to contribute or report issues!

---

# ⚡ Shotgrid AI MCP Server

**Ultra-Performance AI-Enhanced FastAPI-MCP Integration for Flow Production Tracking (Shotgrid) 🚀**

> A blazing-fast, context-aware server powered by AI for Shotgrid production tracking workflows.
> **Built with ❤️ on top of FastAPI-MCP.**

---

## ✨ Key Features

* ⚡ **Ultra-Performance** with `fastapi-mcp`
* 🔁 **Context-aware AI automation** for project and shot creation
* 🛠 **Full CRUD** for Projects, Shots, Assets, Tasks, and Users
* 🖼 **Smart Thumbnail Management** — upload/download made seamless
* 🌐 **Cross-platform compatibility** (Windows, macOS, Linux)
* 📡 **Direct ShotGrid API integration** through FastAPI-MCP
* 💡 **AI-Enhanced Decision Making** for dynamic data operations
* 📦 **Efficient Connection Pooling** for robust scalability

---

## 🤖 AI Demo Workflow

### 🎯 Use Case
> 🧩 **CRUD Everywhere** — full control over all ShotGrid entities
> 🧠 **AI creates a project based on your text prompt**

![AI Project Creation](images/create_project.gif)

> *"Create a shot and attach a thumbnail — in seconds."*

![AI Shot Creation](images/create_shot.gif)

### 🧠 What AI Does:

> 🛠 **Executes a full pipeline of commands** to create a shot and attach a thumbnail
* 🔍 Searches for existing projects
* 🧱 Creates a new shot if not found
* 📝 Generates an automatic description
* 🖼 Uploads a relevant thumbnail

---

## 🎁 Benefits

* ⏱ Saves hours of manual work
* ✅ Prevents duplicate or missed shots
* 🧾 Summarizes every change for transparency
* 🤝 Helps artists, producers, and tech teams stay in sync

---

## 🧠 More AI Magic

![AI Chat](images/chat.gif)

---

## 🔧 Prerequisites

* 🐍 Python **3.9+**
* 🔐 Shotgrid API credentials

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd shotgrid_mcp_project
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root with your ShotGrid credentials:

```env
SHOTGRID_URL=<your-shotgrid-url>
SHOTGRID_SCRIPT_NAME=<your-script-name>
SHOTGRID_SCRIPT_KEY=<your-script-key>
```

---

## 🚀 Running the Server

Start the FastAPI server with hot-reload:

```bash
uvicorn app.main:app --reload
```

📍 Visit: [http://localhost:8000](http://localhost:8000)
📘 Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔗 MCP Client Integration & Configuration

This AI-powered FastAPI-MCP server can be seamlessly integrated with any tool that supports the **Model Context Protocol (MCP)** — including popular tools like **Windsurf** and **Cursor**.

Just point your MCP-compatible client to the server URL:

```json
{
  "mcpServers": {
    "fastapi-mcp": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

### 📌 Tool-specific notes:

* 🌊 **Windsurf** expects the key to be `"serverUrl"`:

  ```json
  {
    "mcpServers": {
      "fastapi-mcp": {
        "serverUrl": "http://localhost:8000/mcp"
      }
    }
  }
  ```

* 🖱️ **Cursor** uses `"url"` as shown in the generic example above.

> 🔧 Replace `"fastapi-mcp"` with any name you like — it will appear as the server label in your client UI.

---

## 🧠 LLM Compatibility

Our server supports **any Large Language Model (LLM)** that *has been trained for tool use* (e.g., with OpenAI's Function Calling, OpenTools, Toolformer, etc.).

### ✅ Works with:

* 🔗 Any LLM that can handle structured tool calls via MCP
* ⚙️ Local and remote language models
* 🧩 Agent frameworks with tool plugins

### 📦 Example Setup

In our demo, we used the following toolchain:

* **LLM Server**: [`LM Studio`](https://lmstudio.ai/) running a local model
* **Client UI**: [`DeepChat`](https://github.com/ThinkInAIXYZ/deepchat) — a beautiful, extensible open-source chat interface

> 🗨️ With this combo, the LLM can talk directly to the ShotGrid API and automate production tasks through natural conversation.

---

## ✅ Running Tests

```bash
pytest tests/
```

---

## 🔌 API Endpoints

| Entity   | Endpoint     | Supported |
| -------- | ------------ | --------- |
| Projects | `/projects/` | CRUD      |
| Assets   | `/assets/`   | CRUD      |
| Shots    | `/shots/`    | CRUD      |
| Tasks    | `/tasks/`    | CRUD      |
| Users    | `/users/`    | CRUD      |

🧠 **All routes are context-aware and enhanced via MCP (Model Context Protocol)**

---

## 🗂 Project Structure

```bash
shotgrid_mcp_project/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas/
│   │   ├── project.py, asset.py, ...
│   ├── routers/
│   │   ├── project.py, shot.py, ...
│   ├── services/
│       ├── shotgrid.py
├── tests/
│   ├── test_project.py, ...
├── .env
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

PRs and ideas are welcome! Feel free to fork, enhance, or reach out.

---

## 💬 Contact

For questions, feedback or collaboration, open an issue or ping me on GitHub.

---
