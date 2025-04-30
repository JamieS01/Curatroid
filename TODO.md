# Curatroid Development Plan (MVP)

This file outlines the development phases and task list for Curatroid's minimum viable product.

---

## Phase 0: Project Setup

- [x] Create GitHub repository and `README.md`
- [x] Define MVP scope (LaunchBox only)
- [x] Sketch initial code and folder structure
- [ ] Define `requirements.txt` with pinned package versions

---

## Phase 1: Configuration

- [x] Create `config.ini` for global settings (frontend, API credentials)
- [ ] Create `preferences.ini` for metadata-based scoring preferences
- [ ] Implement `config_loader.py`
  - [ ] Load and validate config values
  - [ ] Provide safe defaults
  - [ ] Handle missing or insecure credential warnings

---

## Phase 2: Game List Ingestion

- [x] Identify LaunchBox metadata source: `Files.xml`
- [ ] Implement `launchbox.py`
  - [ ] Parse XML and extract name, path, platform
  - [ ] Return normalized `Game` dataclass or dict
- [ ] Define `Game` object with:
  - [ ] `name`, `platform`, `rom_path`, `file_name`
  - [ ] Fields for `metadata`, `score`

---

## Phase 3: API Clients

### IGDB Client

- [ ] Load client ID and secret from config
- [ ] Authenticate and cache token
- [ ] Implement `search_game()` with flexible query
- [ ] Implement `get_metadata_by_id()`

### ScreenScraper Client

- [ ] Load credentials from config
- [ ] Implement `search_game()` with fallback logic
- [ ] Implement `get_metadata()` for full result

---

## Phase 4: Metadata Enrichment

- [ ] Implement `scrape_game.py` or `enricher.py`
  - [ ] Iterate over games from ingest
  - [ ] Check for existing cache
  - [ ] Query APIs as needed
  - [ ] Attach metadata to game object
- [ ] Add error handling and retries
- [ ] Add logging of failed lookups

---

## Phase 5: Metadata Store

- [ ] Implement `metadata_store.py`
  - [ ] Save metadata (initially JSON-based)
  - [ ] Load metadata when available
- [ ] Integrate store into enrichment step

---

## Phase 6: Scoring Engine

- [ ] Implement `scorer.py`
  - [ ] Normalize metadata fields
  - [ ] Apply weights from `preferences.ini`
  - [ ] Compute and assign game scores

---

## Phase 7: Output Writers

- [ ] Implement `csv_writer.py`
  - [ ] Output full metadata and score to CSV
- [ ] Implement `launchbox_xml.py`
  - [ ] Write top-N games to a LaunchBox-compatible playlist XML

---

## Phase 8: Main Runner

- [ ] Implement `__main__.py`
  - [ ] Load config and preferences
  - [ ] Parse game list
  - [ ] Enrich metadata
  - [ ] Score games
  - [ ] Output results

---

## Phase 9: Post-MVP

- [ ] Add unit tests for critical components
- [ ] Refactor API clients (e.g. shared base class, rate-limit decorators)
- [ ] Migrate metadata cache to SQLite with SQLModel
- [ ] Introduce logging configuration
- [ ] Create basic GUI for config (Tkinter or PySimpleGUI)
- [ ] Add support for RomVault, EmulationStation, Pegasus, RomM
- [ ] Add multithreading or async support for scraping

