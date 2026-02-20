<h1 align="center">🚀 Telegram Service Message Cleaner</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" alt="Telegram Bot" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Structural-Governance-FFD700?style=for-the-badge&logo=governance" alt="Structural Governance" />
</div>

<p align="center">
  <strong>The Ultimate Administrative Tool for Telegram Group Governance.</strong><br />
  Automatically purge clutter, maintain chat hygiene, and enforce a clean communication environment.
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/beydah/Telegram-Bot_Message-Cleaner/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Security Policy](https://img.shields.io/badge/Security-Policy-red.svg)](SECURITY.md)

</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [🌟 Project Overview](#-project-overview)
- [✨ Core Features](#-core-features)
- [🏗️ Architectural Integrity](#️-architectural-integrity)
  - [📁 Directory Hierarchy](#-directory-hierarchy)
  - [🏛️ Coding Rules (MANDATORY)](#️-coding-rules-mandatory)
- [🛠️ Technical Stack](#️-technical-stack)
- [⚙️ Rapid Deployment](#️-rapid-deployment)
  - [1️⃣ Prerequisites](#1️⃣-prerequisites)
  - [2️⃣ Installation](#2️⃣-installation)
  - [3️⃣ Configuration](#3️⃣-configuration)
  - [4️⃣ Booting](#4️⃣-booting)
- [📜 Command Reference](#-command-reference)
- [🛡️ Security Governance](#️-security-governance)
- [📈 Roadmap \& Future](#-roadmap--future)
- [🤝 Contributing](#-contributing)
- [⚖️ License](#️-license)

---

## 🌟 Project Overview

**Telegram Service Message Cleaner** is not just a deletion bot; it is a **structural governance engine** for Telegram groups. In high-traffic communities, service messages like "X joined the group" or "Y changed the photo" create noise that buries actual value. This bot serves as a silent janitor, ensuring that your community's focus remains on what matters most: **the conversation.**

## ✨ Core Features

| Feature                     | Description                                     | Benefit                                |
| :-------------------------- | :---------------------------------------------- | :------------------------------------- |
| **Real-Time Purge**         | Instantly deletes incoming service messages.    | Zero chat clutter.                     |
| **Bulk Historical Cleanup** | Scans and removes up to 1000 past messages.     | One-click group restoration.           |
| **Admin Enforcement**       | Strict permission checks for all commands.      | Preventing unauthorized abuse.         |
| **Domain-Driven Design**    | Modular codebase following enterprise patterns. | Easy to scale and maintain.            |
| **Advanced Logging**        | Standardized traceability for all operations.   | Transparent infrastructure management. |

## 🏗️ Architectural Integrity

This project strictly adheres to **Enterprise Structural Governance**:

### 📁 Directory Hierarchy
```text
root/
├── backend/            # The Logic Hub
│   ├── src/
│   │   ├── core/       # Infrastructure (Config, Logger, Boot)
│   │   └── cleaner/    # Domain Logic (Handlers, Verification)
│   └── main.py         # Standardized Entry Point
├── config/             # Security & Environment Templates
├── docs/               # Technical Manuals & Policy
└── tests/              # Quality Assurance Suite
```

### 🏛️ Coding Rules (MANDATORY)
- **Regional Segmentation**: Every file must contain regions (`HEADER`, `LIBRARIES`, etc.).
- **Naming Normalization**: Prefix-based identifiers (`F_` for functions, `C_` for classes).
- **Density Limiting**: Structural constraints to prevent folder/file entropy.

## 🛠️ Technical Stack

- **Primary Language**: [Python 3.8+](https://www.python.org/)
- **API Framework**: [python-telegram-bot v20.7+](https://python-telegram-bot.org/)
- **Infrastructure**: [python-dotenv](https://github.com/theskumar/python-dotenv) for secret shielding.
- **Standards**: PEP 8 compliance with custom Enterprise Overlays.

## ⚙️ Rapid Deployment

### 1️⃣ Prerequisites
- **Python**: 3.8 or higher.
- **Telegram Bot**: Obtain a token from [@BotFather](https://t.me/botfather).
- **Permissions**: Grant the bot **Admistrator** rights with **Delete Messages** enabled.

### 2️⃣ Installation
```bash
# Clone the repository
git clone https://github.com/beydah/Telegram-Bot_Message-Cleaner.git
cd Telegram-Bot_Message-Cleaner

# Install dependencies within the backend hub
pip install -r backend/requirements.txt
```

### 3️⃣ Configuration
Copy the template and fill in your secrets:
```bash
cp .env.example .env
```
Settings required in `.env`:
- `BOT_TOKEN`: Your private bot API key.
- `GROUP_ID`: The unique ID of your group (must start with `-100`).

### 4️⃣ Booting
```bash
python backend/main.py
```

## 📜 Command Reference

| Command    | Permission | Description                                        |
| :--------- | :--------- | :------------------------------------------------- |
| `/test`    | Any        | Verifies system connectivity and heartbeat.        |
| `/cleanup` | **ADMIN**  | Triggers bulk scan and deletion of past headers.   |
| **Auto**   | Bot        | Monitors chat stream and deletes service messages. |

## 🛡️ Security Governance

- **Secret Shielding**: No tokens are ever logged or hardcoded.
- **Admin Validation**: Every command undergoes a three-layer permission check.
- **Regex Enforcement**: Config variables are validated against Telegram's API patterns.
- **No Inline Comments**: Ensuring a professional, distraction-free codebase.

## 📈 Roadmap & Future

Explore the full [ROADMAP.md](docs/ROADMAP.md) for details on:
- ⚡ **Asynchronous Batching**: Faster historical cleanup.
- 💾 **Persistence Layer**: Support for multi-group configurations.
- ⚛️ **Atomic Frontend**: A web dashboard for visual bot management.

## 🤝 Contributing

Contributions are handled through a strict **Pull Request** flow. Please read the [CONTRIBUTING.md](CONTRIBUTING.md) to understand our regional and naming constraints before submitting code.

## ⚖️ License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for the full legal text.

---

<p align="center"> 
  Crafted with architectural precision by <b>Ilkay Beydah Saglam</b><br />
  <a href="https://beydahsaglam.com">beydahsaglam.com</a> 
</p>
