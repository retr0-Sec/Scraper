# 🧠 Scraper de Notícias CNN Brasil - Hacker News Notifier

Este script coleta automaticamente as últimas manchetes relacionadas a **hacking** e **segurança digital** publicadas na CNN Brasil e as envia por **e-mail** para o usuário que executou o script.

> ⚠️ Este projeto é **educacional** e **não deve** ser usado para fins de spam ou automação maliciosa.

---

## 🚀 Funcionalidades

- Coleta de manchetes do portal [CNN Brasil - Hacker](https://www.cnnbrasil.com.br/tudo-sobre/hacker/)
- Validação de e-mail do usuário via regex
- Envio automatizado das notícias por e-mail (via SMTP)
- Interface interativa no terminal
- Uso de variáveis de ambiente com `python-dotenv`

---

## 🧩 Requisitos

- Python 3.8+

---

## ⚙️ Instalação com Poetry

```bash
git clone https://github.com/seuusuario/cnn-hacker-news-emailer.git
cd cnn-hacker-news-emailer

poetry install
