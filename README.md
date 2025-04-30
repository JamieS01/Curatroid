# Curatroid

Curatroid is a recommendation engine for ROM hoarders. It parses a user's ROM library, enriches it with metadata from IGDB and ScreenScraper, and scores each game based on user-defined preferences. It outputs a curated game list suitable for consumption by frontends such as LaunchBox.

This project is in early development. The MVP focuses on LaunchBox support and basic metadata scoring.

## Goals

- Parse game lists from supported frontends (LaunchBox for MVP)
- Scrape metadata from IGDB and ScreenScraper APIs
- Store enriched metadata in a persistent cache
- Allow the user to define preferences for each metadata field
- Score games based on normalized user preferences
- Export a curated selection of games to CSV or LaunchBox playlist format

## MVP Scope

### Configuration
- `config.ini` defines global settings, frontend type, and API credentials
- `preferences.ini` defines weights and filters for scoring

### Ingestion
- Parse `Files.xml` from LaunchBox to extract game name, path, and platform

### API Clients
- IGDB client:
  - Load credentials
  - Authenticate and cache token
  - Search by attributes (e.g. name, filename, hash)
  - Query full metadata by ID

- ScreenScraper client:
  - Load credentials
  - Search and retrieve metadata

### Metadata Storage
- Centralized store for all enriched game metadata
- Avoid redundant queries across sessions

### Scoring
- Apply user preferences
- Normalize and compute a final score per game

### Output
- Write results to CSV
- Generate LaunchBox-compatible playlist XML

## Future Plans
- Support for RomVault, EmulationStation, Pegasus, and RomM
- GUI for configuration and preference management
- Advanced recommendation algorithms
- Secure credential storage
- Plugin support for custom frontends and export formats

## Contributing

If you would like to support or contribute to this project, please feel free to reach out. I am open to collaboration, feedback, and ideas.
