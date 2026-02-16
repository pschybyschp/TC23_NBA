<img width="625" height="444" alt="image" src="https://github.com/user-attachments/assets/e26b5699-2f88-471d-a861-4d9560987f89" />

# 🏀 TC23 NBA — G.O.A.T. Analytics

> **Tableau Conference 2023 — Hands-On Lab**
> Supercharge your Tableau dashboards with Python-powered NBA analytics using [TabPy](https://github.com/tableau/TabPy).

---

## Overview

This repository contains the companion code and datasets for the **Tableau Conference 2023 (TC23)** hands-on lab session. It demonstrates how to integrate Python scripts into Tableau via **TabPy** (Tableau Python Server) to build advanced NBA visualizations — from shot charts and trellis plots to Twitter sentiment analysis.

## Repository Contents

| File | Description |
|------|-------------|
| `Leaguegamelog_Trellis.py` | Fetches NBA league game logs for 7 seasons (2016–17 → 2022–23) via the `nba_api` and returns the data for a **trellis chart** in Tableau. |
| `Player_Shotchart_Hexbin.py` | Pulls detailed shot chart data for selected superstars (Stephen Curry, Kevin Durant, LeBron James) to create **hexbin shot maps**. |
| `Team_Shotchart_Pareto.py` | Retrieves team-level shot chart data (Bulls, Knicks, Lakers, Mavericks) for building **pareto-style shot visualizations**. |
| `Sentiment.py` | Performs **sentiment analysis** on scraped tweets — cleans text, counts word frequencies, and classifies sentiment (positive / negative / neutral) using TextBlob. |
| `Airmovie_scraped_tweets.csv` | Pre-scraped tweet dataset for sentiment analysis. |
| `Data23scraped_tweets.csv` | Additional scraped tweet dataset. |
| `league_data_trellis.csv` | Pre-fetched league game log data (for offline use). |
| `player_data_hexbin.csv` | Pre-fetched player shot chart data (for offline use). |
| `team_data_pareto.csv` | Pre-fetched team shot chart data (for offline use). |
| `basketball-court-lines.png` | Court overlay image for shot chart visualizations. |
| `hex_solid.png` | Custom hex shape for hexbin chart rendering. |
| `Lab Instructions.pdf` | Step-by-step lab guide. |
| `tabpy install instruction.rtf` | TabPy installation instructions. |

## Architecture

