# Curatroid

Curatroid is a recommendation engine for ROM hoarders. It parses a user's ROM library, enriches it with metadata from IGDB and ScreenScraper, and scores each game based on user-defined preferences. It outputs a curated game list suitable for consumption by frontends such as LaunchBox.

This project is in early development. The MVP focuses on LaunchBox support and basic metadata scoring.

## Goals

- Parse game lists from supported frontends
- Scrape metadata from IGDB and ScreenScraper APIs
- Store enriched metadata in a persistent cache
- Allow the user to define preferences for each metadata field
- Score games based on normalized user preferences
- Export a curated selection of games to CSV or LaunchBox playlist format

## Future Plans
- Support for RomVault, EmulationStation, Pegasus, and RomM
- GUI for configuration and preference management
- Secure credential storage

## Contributing

If you would like to support or contribute to this project, please feel free to reach out. I am open to collaboration, feedback, and ideas.
