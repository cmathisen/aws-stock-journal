# AWS Stock Trading Journal

A cloud-native stock journal application built to practice and demonstrate AWS serverless architecture patterns.

## Goals
- Replace a manual spreadsheet-based journal with a lightweight web + API workflow
    - See: https://docs.google.com/spreadsheets/d/1JYuFqA9rfo7pahoipgd-pHQJ19Dp2gT7eKDh6nfqgE4/edit?usp=sharing
- Emphasize reliability, auditability, and clean data modeling
- Practice AWS services and infrastructure-as-code patterns

## Architecture (current)
- Static front-end hosted in S3
- API Gateway receives buy events
- Lambda validates and transforms requests
- SNS/SQS used for decoupling and buffering
- Lambda consumer persists events into DynamoDB

## Tech
- AWS: S3, API Gateway, Lambda, SNS, SQS, DynamoDB
- Language: Python
- IaC: CloudFormation

## Status
In active development, see Roadmap

## Notes
This is a personal learning/portfolio project. It does not place trades or interact with brokerage APIs.
Architecture, service selection, and data flows were designed and implemented manually. AI tools were and
are used selectively to accelerate non-core tasks, similar to how modern engineers use documentation, -
examples, and automation tools in real-world development.

## Roadmap / TODO

Planned improvements and extensions:

### Frontend
- Client-side validation and improved error messaging
- Trade list view with filtering and sorting
- Edit and sell workflows tied to existing buy records
- Improved UX polish and accessibility

### Backend
- Harden server-side validation for all inputs
- Persist trades into DynamoDB with a clean schema
- Support partial and full sell transactions
- Idempotency and replay protection

### Infrastructure
- CloudFormation templates for full environment provisioning
- Optional SAM-based deployment workflow
- Containerized services for ECS-based experiments
- CI/CD pipeline

### Observability & Operations
- Structured logging
- Dead-letter queues
- Basic metrics and alarms

This roadmap is intentionally incremental; the project is designed as a learning and portfolio artifact rather than a production trading system.