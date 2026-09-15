# Error Log Alert Service

This basic log alert microservice studies the use of webhooks to send error alerts from a log source to communication apps like Discord and Slack to notify developments teams and design teams

<img width="485" height="300" alt="image" src="https://github.com/user-attachments/assets/9579c1a6-5bbe-4f52-9cf1-74504310b0a6" />
<img width="332" height="300" alt="image" src="https://github.com/user-attachments/assets/eab46c6b-060c-44ad-835c-58ff62ae3e61" />

Using basic packages in Python managed and run by uv, this small alert microservice features clear separation of responsibility spread across multiple internal services. This exercise mirrors cloud services like AWS's CloudWatch Logs, SQS, and SNS to alert teams and helps developers and stakeholders to make decisions that affect the trajectory of an application. As an added benefit from the architecture, developers can easily attach this alert module to any application by adding database logic and adding webhook urls as environment variables. As a study of webhooks and architecture, this microservice acts a strong case for modularity and microservice based design choices.

## The Stack

Language: Python
Package Manager: uv
Environment Variables: dotenv

## What This Build Has Taught Me

Integrating external software through webhooks
Modular design for easy implementations

## Get Started

Python --version

git clone or GitHub

#### Reminder

Follow .env.example to add environment variables for the appropriate webhook/communication app. 

## Next Steps

Integrating the logs with an LLM that supports Natural Language Processing (NLP) to pinpoint user painpoints
Combining logs with reviews and suggestions to generate business insights for leadership decisions
