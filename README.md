# Drawdown & Consolidation Return Analyzer

![GitHub](https://img.shields.io/github/license/iampratyush4/Drawdown-and-consolidation-return)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Advanced toolkit for analyzing investment drawdown patterns and consolidation returns, incorporating modern portfolio theory and sequence-of-returns risk analysis.

## 📌 Project Overview

This repository provides institutional-grade tools for:
- Maximum drawdown (MDD) calculation and visualization
- Consolidation return period analysis
- Sequence risk modeling using historical and Monte Carlo simulations
- Drawdown-implied correlation analysis :cite[10]
- Retirement portfolio sustainability modeling :cite[4]:cite[6]

Key applications include:
- Portfolio stress testing
- Retirement income planning
- Asset allocation optimization
- Risk-adjusted performance evaluation

## 🛠 Features

### Core Analytics
- **Drawdown Metrics**
  - Maximum Drawdown (MDD)
  - Conditional Drawdown at Risk (CDaR) :cite[9]
  - Time-to-recovery analysis
  - Drawdown heatmaps (magnitude vs duration)

- **Consolidation Analysis**
  - Return distribution during recovery periods
  - Volatility clustering detection
  - Regime shift identification

- **Portfolio Modeling**
  - Safe withdrawal rate simulations :cite[6]
  - Sequence risk analysis using historical scenarios :cite[4]
  - Drawdown-implied correlation matrices :cite[10]

### Advanced Tools
- Monte Carlo simulation engine with customizable:
  - Return distributions (normal, student-t, skewed)
  - Autocorrelation structures
  - Volatility regimes

- Integration with:
  - Yahoo Finance API
  - FRED economic data
  - Custom portfolio inputs

## ⚙️ Installation

1. **Clone Repository**:
   ```bash
   git clone https://github.com/iampratyush4/Drawdown-and-consolidation-return.git
   cd Drawdown-and-consolidation-return
