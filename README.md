# Et-Config (Simplified)

This application provides a web-based interface wrapping the core `et-config` compilation utility pipeline. 

---

## How it Works

1. **Upload / Trigger**: The user imports a profile configuration`.csv` directly and selects how to run the program (options 1 to 3).
2. **Sandbox Environment**: The app isolates execution by provisioning a dedicated thread working environment in `temp_runs/`.
3. **Stage 1 (Shell Automation)**: Calls `logic-repo/sales/newMagicSales.sh` to extract the baseline profile name and generate formatted operational rows.
4. **Stage 2 (Compilation Backend)**: Automatically pipes values down into `logic-repo/scripts/buildCfg.py` utilizing math validation overrides for empty cells and bitwise calculations.
5. **Option 1**: Calls both Stage 1 and Stage 2 commands.
6. **Option 2**: Calls only Stage 1 command.
7. **Option 3**: Calls only Stage 2 command.
8. **Asset Distribution**: Packages output assets into a structured `.zip` or `.csv` framework format and delivers them immediately to the user's downloads folder.

---

## Local Setup

### 1. Prerequisites
- **Node.js (v18+)**
- **Python 3.10+**
- **Bash/Shell**

### 2. Installation
Clone the repository and navigate into the folder:
```bash
git clone https://github.com/jhepburn-hue/Et-Config-Simplified.git
cd et-config-simplified
```

Install the local Node dependency environment and Electron CLI tools:
```bash
npm install
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

### Running Locally

Start the Flask server:
```bash
python3 app.py
```

Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```
