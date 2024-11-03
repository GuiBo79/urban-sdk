# Urban Data Analysis and Visualization Task

## Overview

This project demonstrates the use of spatial data analysis with PostgreSQL (PostGIS extension) and visualizes the results on a Mapbox map. Using geospatial data about road segments, the project explores various PostGIS functions, spatial queries, and data processing techniques to extract meaningful insights from urban infrastructure datasets.

## Project Structure

- **Database Setup**: PostgreSQL with the PostGIS extension to store and query geospatial data
- **Data Processing**: SQLAlchemy and GeoAlchemy2 for data interaction, alongside pandas for data analysis
- **Visualization**: Mapbox GL for interactive maps, showing traffic information and road segment characteristics

## Requirements

### Docker Setup

- Docker (for containerized setup)
- Docker Desktop or Docker installed on your machine
- A Dockerfile and Docker Compose setup are provided to run:
  - PostgreSQL with PostGIS
  - Jupyter Notebook with Mapbox
  - Python dependencies

### Dependencies

- Python 3.8+
- Libraries:
  - pandas
  - SQLAlchemy
  - GeoAlchemy2
  - shapely
  - mapboxgl
  - requests
  - sklearn

## Setup and Installation

1. Clone the repository:

  ```
    git clone https://github.com/yourusername/urban-data-analysis.git
    cd urban-data-analysis
  ```


2. Run Docker Compose:

  ```
    docker-compose up
  ```


3. Initialize the Database:

  ```
    docker-compose run init-db
  ```

## Key Features

1. Spatial Queries in PostGIS
PostGIS allows for sophisticated geospatial queries directly in PostgreSQL:

Roads within a Bounding Box

```
SELECT DISTINCT
    road_name,
    ST_AsText(geometry) AS geometry_text
FROM
    link_info
WHERE
    geometry && ST_MakeEnvelope(-81.7, 30.2, -81.5, 30.4, 4326)
AND
    road_name <> 'None';
```

2. Visualization with Mapbox GL
Choropleth Visualization

Interactive overlays with road details

Example:

```
from mapboxgl.viz import ChoroplethViz

viz = ChoroplethViz(
    geojson_data,
    access_token=mapbox_token,
    color_property="avg_speed",
    color_stops=color_stops,
    center=(-81.6556, 30.3322),
    zoom=10
)
viz.create_html('map_visualization.html')
```

3. Data Analysis and Modeling
Feature Engineering : Creating new features for non-linear relationships

Predictive Modeling : Using RandomForestRegressor for speed prediction

Performance Metrics : Evaluation using MSE and R² Score

Usage
Running Jupyter Notebook
Start Docker Compose

Access Jupyter at <http://localhost:8888>

Running PostGIS Queries
Use database connection in Jupyter

Execute queries in SQL cells or Python using SQLAlchemy

Reference example_queries.sql for sample queries

Contributing
Feel free to contribute by:

Creating pull requests

Opening issues for discussions

Suggesting improvements

Reporting bugs

License
This project is licensed under the MIT License.
