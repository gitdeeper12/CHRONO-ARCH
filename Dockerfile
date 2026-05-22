# CHRONO-ARCH v1.0.0
# Computational Framework for Temporal Archaeology

FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY data/ ./data/
COPY config/ ./config/

# Set environment variables
ENV CA_LOG_LEVEL=INFO
ENV CA_OUTPUT_DIR=/app/output

# Create output directory
RUN mkdir -p /app/output

# Default command
CMD ["python", "-c", "from chrono_arch import __version__; print(f'CHRONO-ARCH v{__version__} ready')"]
