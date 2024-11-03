# Dockerfile for Jupyter Notebook with mapboxgl
FROM jupyter/scipy-notebook:latest

# Switch to root to install system dependencies
USER root

# Install libpq-dev for PostgreSQL and other required libraries
RUN apt-get update && apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install mapboxgl pandas scikit-learn sqlalchemy psycopg2-binary GeoAlchemy2 shapely

# Set up work directory
WORKDIR /home/jovyan/work

# Expose the port for Jupyter Notebook
EXPOSE 8888
