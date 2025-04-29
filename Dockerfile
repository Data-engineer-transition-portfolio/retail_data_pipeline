# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ src/
COPY data/ data/
COPY tests/ tests/
COPY notebooks/ notebooks/

# Environment Variables (Optional if using .env)
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "src/extract.py"]