# Et-Config (Web Wrapper)

This application is a web-based interface for the `et-config` logic. It allows users to upload a CSV, processes it through a two-stage pipeline (Shell script + Python logic), and provides a downloadable ZIP file containing the generated configurations.

## How it Works
1. **Upload**: User provides a `.csv` file via the web UI.
2. **Sandbox**: The app creates a unique temporary directory in `temp_runs/`.
3. **Stage 1**: Runs `logic-repo/sales/newMagicSales.sh`.
4. **Stage 2**: Runs `logic-repo/scripts/buildCfg.py`.
5. **Output**: Zips the results from `logic-repo/configs/nonApproved/WS` and serves it to the user.

---

## Local Setup

### 1. Prerequisites
- **Python 3.10+**
- **Bash/Shell**

### 2. Installation
Clone the repository and navigate into the folder:
```bash
git clone https://github.com/jhepburn-hue/Et-Config-Web.git
cd et-config-web
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install all dependencies:

```bash
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
