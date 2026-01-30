
# AI-powered Kubernetes Scheduler

This repository demonstrates **three AI-specific Kubernetes scheduling approaches**:

1. Reinforcement Learning–based Scheduler (PPO)
2. GPU-aware AI Scheduler (DCGM / Prometheus metrics)
3. Production-grade Kubernetes Scheduler Plugin (Go)

## Architecture
Pod (schedulerName=ai-scheduler)
   → AI Scheduler
   → Metrics (CPU/GPU/Node)
   → AI Model
   → Node Binding

## Use cases
- GenAI / LLM inference
- Distributed ML training
- GPU cost optimization
