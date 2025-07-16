<p align="center">
  <img src="pf_icon.jpg" alt="PrivForge Icon" width="100%" height='auto' />
</p>

<p align="center">
  <a href="https://ko-fi.com/amiandevsec" target="_blank" rel="noopener">
    <img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me a Coffee at Ko-fi" style="height: 45px;" />
  </a>
  <br />
  <em>If you find PrivForge useful, consider supporting development with a coffee ☕️</em>
</p>

# PrivForge (pf) 🛠️

[![GitHub Release](https://img.shields.io/github/v/release/AmianDevSec/PrivForge)](https://github.com/AmianDevSec/PrivForge/releases/latest)

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
