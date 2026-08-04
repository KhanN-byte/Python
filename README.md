# Python Utilities

A curated collection of Python exercises and small utilities focused on API integration, automation, file handling, security fundamentals, and object-oriented programming.

This repository documents practical, hands-on development work. Each folder is self-contained and intended to demonstrate a specific concept or integration.

## Project highlights

| Project | What it demonstrates |
| --- | --- |
| [Currency Exchange Rate](./currency-exchange-rate) | REST API requests, JSON parsing, and currency conversion |
| [Weather App](./weather-app) | Command-line input and OpenWeatherMap integration |
| [Top World News](./Top%20World%20News) | NewsAPI integration and formatted headline output |
| [Send Email](./SendEmail) | SMTP email delivery |
| [WhatsApp Messaging](./WhatsApp%20Messaging) | Twilio messaging and response polling |
| [Security Utilities](./Security_Stuff) | Introductory security-focused scripting |
| [OS Shutdown](./OS_Shutdown) | Operating-system automation |
| [Secure PDF](./securePDF.py) | PDF protection and file processing |

Additional files cover classes, account modeling, savings calculations, Linux commands, and general Python practice.

## Getting started

Clone the repository and create an isolated Python environment:

```bash
git clone https://github.com/KhanN-byte/Python.git
cd Python
python3 -m venv .venv
source .venv/bin/activate
```

Install only the packages required by the example you want to run, then execute that script from the repository root.

For example:

```bash
python3 space_facts.py
```

## Configuration and credentials

Some projects connect to third-party services and require API credentials. Keep credentials outside source control and use environment variables or a local ignored configuration file.

Never commit API keys, access tokens, passwords, or personal information. If a credential is exposed, revoke it immediately and issue a replacement.

## Repository status

These programs are educational utilities and experiments, not production services. They are maintained as a record of practical Python development and continued learning.

## Author

**Haris Khan**  
[GitHub](https://github.com/KhanN-byte) · [LinkedIn](https://www.linkedin.com/in/khan-haris/)
