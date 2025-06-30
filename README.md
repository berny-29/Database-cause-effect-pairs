# Causal Data Pairs Database

A comprehensive collection of causal data pairs extracted from USGS (United States Geological Survey) environmental monitoring data, formatted for causal inference research and machine learning applications. The data follow the Tübingen style format. 

## Overview

This repository contains 38 different types of causal relationships derived from USGS environmental data, including meteorological, hydrological, and water quality measurements. Each pair represents a scientifically established cause-effect relationship in environmental systems.

## Dataset Statistics

- **Total Causal Relationships**: 38 types
- **Total Data Pairs**: 85 individual pairs
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

x1 y1
x2 y2
x3 y3

Where `x` represents the cause variable and `y` represents the effect variable, separated by a single space.

## Data Quality Notes

### High Quality Pairs (Recommended)
- Air Temperature → Water Temperature (2 pairs)
- Water Temperature → Dissolved Oxygen (4 pairs)
- Wind Speed → Evaporation (2 pairs)
- Streamflow → Water Level (2 pairs)

### Moderate Quality Pairs
- Solar Radiation → Water Temperature (timing challenges)
- Precipitation → Reservoir Storage (complex relationships)

### Limited Data Pairs (Use with caution)
- Wind Speed → Turbidity (1 pair only)
- Precipitation → Turbidity (1 pair only)
- Rainfall → Chemical Dilution (1 pair only)

