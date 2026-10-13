# Empirical Evaluation of AI Techniques in Human-Robot Interaction

### Verbal and Non-Verbal Cues Using LLMs, Computer Vision, and Rule-Based Systems

## Overview

This project investigates how different artificial intelligence techniques influence verbal and non-verbal communication in human-robot interaction (HRI).

Using the Furhat social robot, three AI approaches were explored: Large Language Models (LLMs), computer vision using convolutional neural networks (CNNs), and rule-based systems.

The project combines AI implementation with an empirical pilot study to examine how different approaches influence users' perceptions of robot naturalness, trust, intelligence, responsiveness, and engagement.

**Course:** CS 686 – Introduction to Artificial Intelligence  
**Institution:** University of Waterloo  
**Project Type:** AI Implementation and Empirical Pilot Study

## Research Objectives

- Compare different AI techniques for supporting human-robot interaction.
- Investigate verbal and non-verbal behaviours generated through different computational approaches.
- Examine user perceptions of robot interaction across AI conditions.
- Compare implementation complexity, controllability, and perceived interaction quality.

## AI Techniques and Implementation

### 1. Large Language Model (LLM)

An LLM-based approach was implemented using the Groq API to generate context-sensitive conversational responses.

The implementation explored prompt design, personality-related responses, and conversational flexibility.

### 2. Computer Vision (CNN)

A computer-vision approach was explored using DeepFace for facial-expression analysis.

The system used visual cues to support robot response adaptation, with template-based verbal responses.

### 3. Rule-Based System

A scripted interaction system was implemented using predefined conversational responses and non-verbal behaviours.

This approach emphasized predictable and controllable robot interactions.

## Experimental Design

The pilot study compared three AI interaction conditions using Furhat robot demonstrations.

Participants were randomly assigned to view one of three interaction videos through an online Qualtrics survey.

The evaluation included demographic questions, seven-point Likert-scale items, and open-ended feedback.

**Participants:** 14 recruited; 11 valid responses reported.

## Evaluation Dimensions

- Perceived naturalness
- Trust
- Intelligence
- Responsiveness
- Engagement
- Implementation complexity
- Ease of use

## Preliminary Findings

The pilot suggested differences in perceived interaction quality and implementation complexity across the three AI approaches.

- **LLM:** More flexible and conversational responses, but greater implementation complexity.
- **Computer Vision:** Visual responsiveness, with challenges involving latency and emotion mirroring.
- **Rule-Based:** Greater predictability and implementation simplicity, but more rigid interactions.

These findings are exploratory due to the small sample size and uneven distribution across experimental conditions.

## Technologies

- Furhat Social Robot
- Python
- Groq API
- DeepFace
- Large Language Models
- Computer Vision
- Rule-Based AI
- Qualtrics

## Future Work

Future work could explore hybrid AI architectures combining visual perception, generative dialogue, and rule-based behavioural constraints.

Larger evaluations and longitudinal studies would also help examine changes in trust, comfort, and engagement over time.

## Project Documentation

This repository contains implementation materials, system documentation, and approved demonstrations associated with the CS 686 pilot project.
