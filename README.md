# Reproducibility Artifact

## Table of Contents

1. [Summary](#1-summary)  
2. [Reproducibility and Execution Instructions](#2-reproducibility-and-execution-instructions)  
3. [FAISS Index and BM25 Databases](#3-faiss-index-and-bm25-databases)  
4. [Document Corpus and Chatbot Scripts](#4-document-corpus-and-chatbot-scripts)  
5. [Reviewer Evaluation Results](#5-reviewer-evaluation-results)  
6. [How to Cite](#6-how-to-cite)

---

## 1) Summary

This repository provides the experimental artifacts supporting the study “Scrum-Guided Development of an Intelligent Payroll Management System with Rule-Based Automation and RAG Chatbot Support,” to appear in Knowledge-Based Systems. It contains the code, datasets, retrieval databases, evaluation results, and scripts required to reproduce the experiments reported in the paper.

The repository includes the chatbot implementation scripts, the regulatory document corpus used for knowledge ingestion (GJU payroll regulations and Jordanian tax law), prebuilt FAISS and BM25 retrieval databases, and evaluation datasets consisting of the full benchmark of 50 questions, including the 18-question subset used during the initial configuration search. It also provides reviewer evaluation results, red-teaming experiments, ER diagrams describing the system reference tables, and Python scripts to reproduce all figures and tables reported in the Validation and Results sections of the paper.

Together, these artifacts enable end-to-end reproduction of the experimental results presented in the study.

---

## 2) Reproducibility and Execution Instructions

All headline figures and tables reported in the paper can be reproduced end-to-end using the scripts provided in this repository. The commands below specify the exact steps required to regenerate the reported results.

### Execution Environment

The scripts were executed and tested using the following environment:

- IDE: Spyder 5.5.2  
- Python: 3.8.10 (64-bit)  
- GUI Framework: Qt 5.15.2 | PyQt5 5.15.10  
- Operating System: Windows 10 Enterprise LTSC  
- Hardware: Processor: 12th Gen Intel® Core™ i7-12700H @ 2.30 GHz; Memory: 32 GB RAM

### Hugging Face Model Access

Some scripts require access to subscription-based Hugging Face large language models.

If a script includes the following line:

```python
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

a valid Hugging Face subscription and API key are required to run that script. These scripts invoke cloud-hosted Hugging Face LLMs via their APIs.

Scripts that do not reference a Hugging Face API key can be executed locally without any subscription.

Commands to Reproduce Reported Results

The commands below correspond to the exact steps required to regenerate the reported results.

# Reproduce Fig. 33 & Fig. 34
python hrpis-10-1-1-scrum/scrum_analysis.py

# Reproduce Fig. 37
python hrpis-10-1-3-operational/salary_cycle_SLA.py

# Reproduce Fig. 38 & Fig. 39
python hrpis-10-1-3-operational/salary_posting_plots.py

# Reproduce Fig. 40
python hrpis-10-1-4-helpdesk/helpdesk-tax-slip-bar.py

# Reproduce Table 13 (see script output)
python pure-llm-anal-10-2-3/paper_anal_multi_pure_llms.py

# Reproduce Fig. 41, Fig. 43, and Fig. 44
python rag-llm-anal-10-2-3-and-10-2-4/paper_anal_multi_rag_llms.py

# Run the script below to reproduce the following table data
# Table 14 & 15 (after run, see plots/winning_combination_per_question.csv )
# Table 16 (after run, see plots/cohen_kappa_per_category_winning_config.csv )
# Table 17 (after run, see plots/config_ranking.csv)
python rag-llm-anal-10-2-3-and-10-2-4/paper_anal_multi_rag_llms.py

# Reproduce stats in section 10.2.5 (see script output)
python rag-vs-pure-gain-stats-10-2-5/rag-hybrid-vs-pure.py

# Reproduce Table 18 (after run, output in plots/cohen_kappa_per_category.csv)
python test-50-questions-10-2-6/paper_anal_winning_rag_cohen_hybrid_trans_50q.py

# Reproduce results in section 10.2.7 (see red-teaming-results.csv for results)
python test-red-teaming-10-2-7/red_teaming.py

3) FAISS Index and BM25 Databases

The repository includes prebuilt vector and lexical retrieval databases used in the chatbot experiments. These indexes allow the RAG-based chatbot to perform document retrieval without regenerating embeddings or rebuilding the retrieval indexes.

FAISS database (all-mpnet-base-v2):

public_dir\2-chatbot-calls\vectordb_multi\vectordb_faiss_750_all-mpnet-base-v2

FAISS database (sentence-transformers/all-MiniLM-L6-v2):

public_dir\2-chatbot-calls\vectordb_multi\vectordb_faiss_750_sentence-transformers_all-MiniLM-L6-v2

BM25 lexical database:

public_dir\2-chatbot-calls\vectordb_multi\vectordb_bm25
4) Document Corpus and Chatbot Scripts
Document Corpus

PDF documents containing the German Jordanian University (GJU) payroll regulations and the Jordanian tax law are provided in the directory:

public_dir\chatbot-ingest\docs

These documents constitute the knowledge source used for document ingestion and retrieval in the RAG-based chatbot experiments.

Chatbot Ingestion Script

The document ingestion pipeline used to preprocess and index the PDF corpus and generate the retrieval databases is located in:

public_dir\chatbot-ingest
Chatbot Invocation Script

The base script used to invoke and evaluate chatbot interactions, including pure LLM, RAG-based, and hybrid configurations, is located in:

public_dir/chatbot-calls
5) Reviewer Evaluation Results

The repository includes reviewer evaluation results for chatbot responses across multiple configurations and models.

The full benchmark consists of 50 evaluation questions. An 18-question subset (Q1–Q18) from this set was used during the initial evaluation phase to compare model configurations with a manageable number of runs. For each configuration, answers were generated over three independent runs and evaluated by two reviewers.

The corresponding result files are:

chatbot_eval_review_pure_llms_results.csv (Pure LLM model results)

chatbot_eval_review_rag_llms_results.csv (RAG-based LLM model results)

chatbot_eval_review_hybrid_only_results.csv (Hybrid retrieval RAG model results)

chatbot_eval_review_hybrid_only_with_trans_results.csv (Hybrid retrieval RAG with query transformation results)

After identifying the best-performing configuration, the evaluation was verified using the full set of 50 questions. The complete dataset of questions and answer keys is provided in the file:

50_questions_with_ans_keys.xlsx

(in this file, the initial evaluation subset corresponds to questions Q1–Q18).

The results generated using the full benchmark are available in the directory:

test-50-questions-10-2-6
6) How to Cite
Repository Citation (BibTeX)
@misc{alhawari2026hrpis,
  author = {Feras Al-Hawari and Anoud Alufeishat and Mohammad Habahbeh and Ahmad Alfalayleh},
  title = {HRPIS and RAG-Based Chatbot Evaluation Artifacts},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/firasalhawari/hrpis_rag_chatbot_evaluation}
}
Example Citation (APA style)

Feras Al-Hawari, Anoud Alufeishat, Mohammad Habahbeh, & Ahmad Alfalayleh. (2026).
HRPIS and RAG-Based Chatbot Evaluation Artifacts [Computer software]. GitHub.
https://github.com/firasalhawari/hrpis_rag_chatbot_evaluation

Corresponding Paper

Feras Al-Hawari, Anoud Alufeishat, Mohammad Habahbeh, & Ahmad Alfalayleh. (2026).
Scrum-Guided Development of an Intelligent Payroll Management System with Rule-Based Automation and RAG Chatbot Support. Knowledge-Based Systems.