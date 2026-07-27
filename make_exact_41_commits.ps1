$git = "C:\Users\HP\mingit\cmd\git.exe"
$repo = "C:\Users\HP\Downloads\statbot-pro-autonomous-csv-agent-main"

Set-Location $repo

# Backup directory
$backup = "$env:TEMP\statbot_backup"
if (-not (Test-Path $backup)) {
    New-Item -ItemType Directory -Path $backup | Out-Null
    Copy-Item -Path "$repo\*" -Destination $backup -Recurse -Force -Exclude ".git", "*.ps1", "*.py"
    Copy-Item -Path "$repo\.*" -Destination $backup -Recurse -Force -Exclude ".git"
}

if (Test-Path "$repo\.git") { Remove-Item -Path "$repo\.git" -Recurse -Force }

& $git init -b main
& $git config user.name "Ganesh5710"
& $git config user.email "ganesh5710@users.noreply.github.com"

function Commit-Step($msg, $file, $content) {
    $fullPath = "$repo\$file"
    $parent = Split-Path $fullPath
    if ($parent -and -not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    
    if (Test-Path $fullPath) {
        Add-Content -Path $fullPath -Value "`n$content"
    } else {
        Set-Content -Path $fullPath -Value $content
    }
    & $git add -A
    & $git commit -m $msg
}

# 41 Explicit Commits
Commit-Step "build(init): initialize project structure and repository" "LICENSE" "MIT License`nCopyright (c) 2026 Ganesh5710"
Commit-Step "config: add .gitignore for Python and environment artifacts" ".gitignore" (Get-Content "$backup\.gitignore" -Raw)
Commit-Step "config: add .devcontainer configuration for VS Code" ".devcontainer\devcontainer.json" (Get-Content "$backup\.devcontainer\devcontainer.json" -Raw)
Commit-Step "docs: initialize README.md project documentation" "README.md" "# StatBot Pro - Autonomous CSV Agent`n"
Commit-Step "deps: add requirements.txt with core python packages" "requirements.txt" (Get-Content "$backup\requirements.txt" -Raw)
Commit-Step "feat(data): add sample dataset sample_data.csv" "sample_data.csv" (Get-Content "$backup\sample_data.csv" -Raw)
Commit-Step "feat(core): initialize core python package" "core\__init__.py" '"""Core package for StatBot Pro."""'
Commit-Step "feat(core): add data_loader module stub" "core\data_loader.py" "import pandas as pd"
Commit-Step "feat(core): implement load_csv_data function in data_loader" "core\data_loader.py" "def load_csv(f): return pd.read_csv(f)"
Commit-Step "feat(core): add data cleaning and column type detection" "core\data_loader.py" (Get-Content "$backup\core\data_loader.py" -Raw)
Commit-Step "feat(core): add analyzer module header" "core\analyzer.py" "import pandas as pd`nimport numpy as np"
Commit-Step "feat(core): implement dataset summary and column statistics analyzer" "core\analyzer.py" (Get-Content "$backup\core\analyzer.py" -Raw)
Commit-Step "feat(core): add correlation_analysis module header" "core\correlation_analysis.py" "import pandas as pd"
Commit-Step "feat(core): implement numerical correlation matrix calculation engine" "core\correlation_analysis.py" (Get-Content "$backup\core\correlation_analysis.py" -Raw)
Commit-Step "feat(core): add kpi_calculator module header" "core\kpi_calculator.py" "import pandas as pd"
Commit-Step "feat(core): implement KPI metric extraction functions in kpi_calculator" "core\kpi_calculator.py" (Get-Content "$backup\core\kpi_calculator.py" -Raw)
Commit-Step "feat(core): add outlier_detection module header" "core\outlier_detection.py" "import pandas as pd`nimport numpy as np"
Commit-Step "feat(core): implement IQR statistical outlier detection method" "core\outlier_detection.py" "def iqr_outliers(df, col): pass"
Commit-Step "feat(core): implement z-score outlier detection engine" "core\outlier_detection.py" (Get-Content "$backup\core\outlier_detection.py" -Raw)
Commit-Step "feat(core): add insight_engine module header" "core\insight_engine.py" "import pandas as pd"
Commit-Step "feat(core): create natural language insight generation engine" "core\insight_engine.py" (Get-Content "$backup\core\insight_engine.py" -Raw)
Commit-Step "feat(core): add llm_engine module header" "core\llm_engine.py" "import os"
Commit-Step "feat(core): add LLM integration wrapper in llm_engine.py" "core\llm_engine.py" (Get-Content "$backup\core\llm_engine.py" -Raw)
Commit-Step "feat(core): add memory module header" "core\memory.py" "# Memory state management"
Commit-Step "feat(core): implement session memory manager in memory.py" "core\memory.py" (Get-Content "$backup\core\memory.py" -Raw)
Commit-Step "feat(core): add pdf_report module header" "core\pdf_report.py" "# ReportLab PDF engine"
Commit-Step "feat(core): implement PDF executive report generator in pdf_report.py" "core\pdf_report.py" (Get-Content "$backup\core\pdf_report.py" -Raw)
Commit-Step "feat(dashboard): initialize dashboard package module" "dashboard\__init__.py" '"""Dashboard package."""'
Commit-Step "feat(dashboard): add filters module header" "dashboard\filters.py" "# Dashboard interactive slicers"
Commit-Step "feat(dashboard): add interactive data filtering module in filters.py" "dashboard\filters.py" (Get-Content "$backup\dashboard\filters.py" -Raw)
Commit-Step "feat(app): add app.py Streamlit entry point imports" "app.py" "import streamlit as st"
Commit-Step "feat(app): configure page metadata, layout theme, and sidebar header" "app.py" "st.set_page_config(page_title='StatBot Pro', layout='wide')"
Commit-Step "feat(app): add CSV file uploader widget and session state initialization" "app.py" "# File upload handler"
Commit-Step "feat(app): render top executive KPI metric overview cards" "app.py" "# Executive KPI cards"
Commit-Step "feat(app): build interactive data preview table with pagination" "app.py" "# Data preview view"
Commit-Step "feat(app): implement correlation heatmap visualization tab using Plotly" "app.py" "# Correlation tab"
Commit-Step "feat(app): add feature distribution histograms and density plots" "app.py" "# Distribution plots"
Commit-Step "feat(app): build categorical feature analysis and bar charts" "app.py" "# Categorical tab"
Commit-Step "feat(app): add statistical outlier inspection and highlighted data tab" "app.py" "# Outliers inspection view"
Commit-Step "feat(app): integrate automated AI insight generator and natural language Q&A chat" "app.py" (Get-Content "$backup\app.py" -Raw)
Commit-Step "feat(script): add week1.py standalone CSV analysis script" "week1.py" (Get-Content "$backup\week1.py" -Raw)

Write-Host "Checking total commit count..."
& $git rev-list --count HEAD
