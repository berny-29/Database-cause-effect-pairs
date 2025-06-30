# USGS Causal Data Pairs Dataset

A comprehensive collection of causal data pairs extracted from USGS (United States Geological Survey) environmental monitoring data, formatted for causal inference research and machine learning applications.

## Overview

This repository contains 38 different types of causal relationships derived from USGS environmental data, including meteorological, hydrological, and water quality measurements. Each pair represents a scientifically established cause-effect relationship in environmental systems.

## Dataset Statistics

- **Total Causal Relationships**: 38 types
- **Total Data Pairs**: 87 individual pairs
- **Data Format**: Space-separated (x y) Tübingen format
- **Domains**: Hydrology, Meteorology, Water Quality, Ecology
- **Time Period**: 2024-2025
- **Data Source**: USGS Water Data for the Nation

## Causal Relationships Categories

### Hydrological
- Precipitation → Stream Flow
- Snow Depth → River Flow  
- Rainfall → Water Level
- Streamflow → Water Level

### Meteorological
- Air Temperature → Water Temperature
- Solar Radiation → Atmospheric Temperature
- Wind Speed → Evaporation
- Barometric Pressure → Gage Height

### Water Quality
- Water Temperature → Dissolved Oxygen
- pH → Chemical Equilibrium
- Turbidity → Aquatic Productivity
- Organic Matter → Oxygen Depletion

### Ecological
- Photosynthetic Activity → Oxygen Production
- Nitrogen Loading → Eutrophication
- Wind Speed → Water Mixing

## Data Format

All data pairs are provided in the Tübingen format:
...
x1 y1
x2 y2
x3 y3
...

