from fastapi import FastAPI

app = FastAPI(
    title="Log Anomaly + Root Cause Analysis",
    description="Metrics-based anomaly detection and root-cause analysis.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
