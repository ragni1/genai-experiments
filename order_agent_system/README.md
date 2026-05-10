# Order Agent System

## Overview
This project demonstrates a simple agentic workflow:
- Read order details from email text
- Parse orders using an AI agent
- Save orders to a local file (ERP simulation)
- Send confirmation or failure messages

## Folder Structure
- agents/ : Contains agent classes (reader, parser, ERP, messaging)
- models/ : Data classes (OrderDetail)
- utils/  : Helper modules (LLM client, logging)
- main.py : Entry point for orchestration

## Installation
- Requires Python 3.10+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
