"""Deterministic LLM call wrapper.

Every LLM call in this project goes through `run()`. The wrapper:

- Pins model id, model version, temperature, seed, top_p.
- Hashes the prompt + system + parameters and uses the hash for caching.
- Logs every call to `04_analysis/llm_call_log.jsonl` with prompt hash,
  response hash, latency, tokens.
- Supports the three model families used in the ensemble:
  `anthropic:claude-opus-4-7`, `openai:gpt-5`, `qwen:qwen3-72b-instruct`.

Real implementation pending. Scaffolded so callers can be written against
its surface.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Optional


ModelId = Literal[
    "anthropic:claude-opus-4-7",
    "openai:gpt-5",
    "qwen:qwen3-72b-instruct",
]


@dataclass(frozen=True)
class LLMRequest:
    model: ModelId
    system: str
    user: str
    temperature: float = 0.0
    top_p: float = 1.0
    max_tokens: int = 2048
    seed: int = 20260531
    extra: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class LLMResponse:
    request_hash: str
    response_hash: str
    text: str
    model_version: str
    prompt_tokens: int
    completion_tokens: int
    latency_ms: int


def run(req: LLMRequest, *, use_cache: bool = True) -> LLMResponse:
    """Execute or replay a single LLM call. Not yet implemented."""
    raise NotImplementedError("Implement when first extraction stage is wired up.")


def prompt_hash(req: LLMRequest) -> str:
    """Stable hash of the request, used for caching and reproducibility."""
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("This module is a library, not a script.")
