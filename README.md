# 🚀 SkyWatch Status Dashboard

[![Modern DevOps Pipeline](https://github.com/radovan-bulna/Status-Dashboard/actions/workflows/main.yml/badge.svg)](https://github.com/radovan-bulna/Status-Dashboard/actions)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**SkyWatch Status Dashboard** je demonštračný DevOps projekt, ktorý slúži na monitorovanie stavu systému v reálnom čase. Aplikácia beží v Docker kontajneri a je plne automatizovaná pomocou GitHub Actions.

## 🛠️ Tech Stack
* **Backend:** Python 3.11, Flask
* **Containerization:** Docker (Slim Debian base)
* **CI/CD:** GitHub Actions
* **Security:** Trivy Vulnerability Scanner, Safety (Dependency Check)
* **Linting:** Flake8 (PEP 8 Compliance)

---

## 🏗️ Architektúra Pipeline
Tento projekt využíva modernú CI/CD pipeline, ktorá zaisťuje kvalitu kódu v niekoľkých krokoch:

1.  **Lint & Audit:** Kontrola štýlu kódu (Flake8) a bezpečnosti knižníc (Safety).
2.  **Docker Build:** Vytvorenie optimalizovaného Docker image.
3.  **Security Scan:** Skenovanie obrazu na prítomnosť zraniteľností pomocou Trivy.
4.  **Integration Test:** Spustenie kontajnera a overenie funkčnosti cez `/health` endpoint.

---

## 🚀 Lokálne spustenie

### Cez Python
```bash
# Inštalácia závislostí
pip install -r requirements.txt

# Spustenie aplikácie
python app.py
