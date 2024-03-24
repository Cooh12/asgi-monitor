from dataclasses import dataclass, field

from prometheus_client import CollectorRegistry

__all__ = ("CommonMetricsConfig",)


def _build_default_registry() -> CollectorRegistry:
    return CollectorRegistry(auto_describe=True)


@dataclass
class CommonMetricsConfig:
    """Configuration class for the Metrics middleware."""

    app_name: str
    """The name of the ASGI application."""

    metrics_prefix: str
    """The prefix to use for the metrics."""

    registry: CollectorRegistry = field(default_factory=_build_default_registry)
    """A registry for metrics, you can also specify a global REGISTRY to support all your current metrics"""

    include_trace_exemplar: bool = field(default=False)
    """Whether to include trace exemplars in the metrics."""

    include_metrics_endpoint: bool = field(default=True)
    """Whether to include a /metrics endpoint."""
