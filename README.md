#    ____       _       ______                    
#   / __ \_____(_)   __/ ____/___  _________ ____ 
#  / /_/ / ___/ / | / / /_  / __ \/ ___/ __ `/ _ \
# / ____/ /  / /| |/ / __/ / /_/ / /  / /_/ /  __/
#/_/   /_/  /_/ |___/_/    \____/_/   \__, /\___/ 
                                    /____/       
# PrivForge (pf) 🛠️

**PrivForge** is a modular **Linux Privilege Escalation Toolkit** written in Python, designed to assist security professionals and penetration testers in identifying and exploiting local privilege escalation vectors.

> ⚡ Lightweight, interactive, and highly effective — use `pf` to launch PrivForge from your terminal.

---

## 🎯 The current version includes these features

- 🧱 **Offline GTFO**: Integrated local GTFOBins-style exploit reference — no need for internet access.
  
- 🎭 **Backdoor Installer**:
  - PAM module injection
  - Netcat-based malicious service installation

- 📁 **PATH Exploitation Toolkit**:
  - Full support for `LD_PRELOAD`, with C language binary injection

- 🌐 **NFS Exploiter**:
  - Shell access via shared mount manipulation

- 🎨 **Beautiful CLI Interface** using the [`Rich`](https://github.com/Textualize/rich) library
- 🔐 **Safe Execution Mode**: Preview before execution to reduce risks on production environments
  
---

## 🚀 Quick Start

### 🔧 Requirements

- Python **3.7+**
- Linux environment
- Optional: `ncat`, `mount`, `gcc`, and other system binaries (depending on exploit module)

### 📦 Installation

```bash
git clone https://github.com/AmianDevSec/PrivForge.git
cd PrivForge
pip install -r requirements.txt
```
