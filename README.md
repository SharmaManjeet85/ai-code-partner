# AI Code Reviewer (Local LLM Powered)

An AI-powered code review tool that analyzes source code using a local Large Language Model and generates structured review reports.

The project uses a Retrieval Augmented Generation (RAG) architecture to provide repository-aware code reviews.

---

## Features

* Local AI code review using Ollama
* Supports multiple programming languages
* Repository-aware reviews using vector embeddings
* Parallel AI analysis for faster execution
* Markdown review report generation
* Works without cloud APIs

---

## Architecture

```
Codebase
   |
   v
Code Scanner
   |
   v
Code Chunker
   |
   v
Embedding Generator
(sentence-transformers)
   |
   v
Vector Database
(ChromaDB)
   |
   v
Context Retrieval
   |
   v
LLM Code Review
(Ollama - DeepSeek Coder)
   |
   v
Review Report Generator
```

---

## Technology Stack

| Component       | Technology                     |
| --------------- | ------------------------------ |
| AI Model        | Ollama (DeepSeek Coder)        |
| Vector Database | ChromaDB                       |
| Embeddings      | sentence-transformers          |
| Language        | Python                         |
| Architecture    | Retrieval Augmented Generation |

---

## Project Structure

```
ai-code-reviewer
│
├── reviewer.py
├── repo_scanner.py
├── code_chunker.py
├── ai_reviewer.py
├── prompt_builder.py
├── vector_store.py
├── repo_indexer.py
├── report_writer.py
│
├── sample_project
│
└── review-report.md
```

---

## Installation

### 1 Install Python dependencies

```
pip install ollama
pip install chromadb
pip install sentence-transformers
pip install rich
```

### 2 Install Ollama

Download and install Ollama.

https://ollama.com/download

---

## Download Code Review Model

```
ollama pull deepseek-coder:6.7b
```

---

## Index the Repository

Before running the reviewer, build embeddings for the repository.

```
python repo_indexer.py ./sample_project
```

---

## Run AI Code Review

```
python reviewer.py review ./sample_project
```

---

## Example Output

```
# AI Code Review Report

File: userService.cs
Line: 12

Issue:
Potential null reference exception

Suggestion:
Ensure database instance is initialized before calling Save()

Severity:
High
```

---

## Supported Languages

Currently supported:

* C#
* Python
* JavaScript
* TypeScript
* Java

---

## Future Enhancements

* GitHub PR integration
* AST-based code analysis
* Architecture rule checking
* Security vulnerability detection
* Code fix suggestions
* CI/CD integration


