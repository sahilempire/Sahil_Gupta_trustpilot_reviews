## Novo Customer Feedback Taxonomy (.md)

This document outlines a hierarchical taxonomy for classifying customer feedback data for Novo. This taxonomy will be used to label feedback and train an intent prediction model.

**Data Source:** [Data] Novo Reviews (Columns: Title, Review Text, Review Date, Date of Experience, rating_processed, Year of Review, Diff in Months)

**Taxonomy Structure:**

This taxonomy utilizes a hierarchical structure with two main levels:

* **Level 1: Main Category:** Broad categories representing major areas of customer interaction with Novo.
* **Level 2: Subcategory:** More specific breakdowns within each Main Category, further defining the nature of customer feedback.

**Sample Taxonomy:**

| Level 1: Main Category | Level 2: Subcategory | Potential Data Source Columns | Reasoning |
|---|---|---|---|
| Account Management | Opening an Account | Review Text, Date of Experience | Reviews mentioning opening process or difficulties. |
| Account Management | Closing an Account | Review Text, Date of Experience | Reviews mentioning account closure or challenges. |
| Account Management | Updating Account Information | Review Text, Date of Experience | Reviews mentioning updating information or encountering issues. |
| Account Management | Login Issues | Review Text, Date of Experience | Reviews mentioning login problems or security concerns. |
| Account Management | Two-Factor Authentication | Review Text, Date of Experience | Reviews mentioning 2FA setup, functionality, or issues. |
| Transactions | Debit Card Transactions | Review Text, Date of Experience, rating_processed | Reviews mentioning debit card usage, declines, or specific transactions. | 
| Transactions | ACH Transfers | Review Text, Date of Experience, rating_processed | Reviews mentioning ACH transfers, failures, or delays. |
| Transactions | Bill Pay | Review Text, Date of Experience, rating_processed | Reviews mentioning bill pay setup, scheduling issues, or payment errors. |
| Transactions | Mobile Deposits | Review Text, Date of Experience, rating_processed | Reviews mentioning mobile deposits, failures, processing times, or specific issues. |
| Transactions | ATM Withdrawals | Review Text, Date of Experience, rating_processed | Reviews mentioning ATM withdrawals, fees, access problems, or specific transactions. |
| Transactions | International Transactions | Review Text, Date of Experience, rating_processed | Reviews mentioning international transactions, conversion rates, or failures. |
| Billing & Statements | Understanding Statements | Review Text | Reviews mentioning difficulty understanding statements or requesting clarifications. |
| Billing & Statements | Fees & Charges | Review Text, rating_processed | Reviews mentioning unexpected fees, disputes, or requesting fee waivers. |
| Billing & Statements | Disputes & Refunds | Review Text, Date of Experience | Reviews mentioning disputes, requesting refunds, or resolution times. |
| Billing & Statements | Transaction History Discrepancies | Review Text | Reviews mentioning missing transactions, incorrect amounts, or discrepancies in statements. |  
| Security & Fraud | Suspicious Activity | Review Text, Date of Experience | Reviews mentioning suspicious activity notifications or reporting process. |
| Security & Fraud | Unauthorized Transactions | Review Text, Date of Experience, rating_processed | Reviews mentioning unauthorized transactions, identifying fraud, or resolving fraudulent charges. |  
| Security & Fraud | Reporting a Lost/Stolen Debit Card | Review Text, Date of Experience | Reviews mentioning reporting lost/stolen cards or replacement process experiences. |
| Security & Fraud | Data Security Concerns | Review Text | Reviews mentioning concerns about app security, data privacy, or security breaches. |  
| Customer Support | Long Wait Times | Review Text | Reviews mentioning long wait times for customer service interactions. |  
| Customer Support | Unhelpful or Unprofessional Service | Review Text | Reviews mentioning negative experiences with customer support interactions. |  
| Customer Support | Difficulty Finding Answers | Review Text | Reviews mentioning difficulty finding answers through support channels. |  
| Customer Support | Feedback on Support Channels (Phone, Email, Chat) | Review Text, Rating_processed | Reviews mentioning specific support channels (phone, email, chat) and experiences. |  
| App Functionality | Bugs & Glitches | Review Text, Title | Reviews mentioning specific app malfunctions or bugs (mentioning features in Title might be helpful). |  
| App Functionality | Difficulty Using Specific Features | Review Text, Title | Reviews mentioning difficulty using specific app features (mentioning features in Title might be helpful). |  
| App Functionality | App Crashes | Review Text | Reviews mentioning frequent app crashes or stability issues. |  
| App Functionality | Suggestions for Improvement | Review Text, Title | Reviews suggesting app improvements, new features, or usability enhancements (mentioning features in Title might be helpful). |  
| General Feedback | Positive Overall Experience | Review Text, Rating_processed | Reviews expressing overall satisfaction with Novo. |  
| General Feedback | Negative Overall Experience | Review Text, Rating_processed | Reviews expressing overall dissatisfaction with Novo. Use subcategories from other categories to identify