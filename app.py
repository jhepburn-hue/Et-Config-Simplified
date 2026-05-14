import os
import shutil
import subprocess
import uuid
from flask import Flask, request, render_template, send_file, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)
os.makedirs('temp_runs', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def run_pipeline():
    file = request.files.get('file')
    if not file or file.filename == '':
        return "No file selected", 400

    original_name = secure_filename(file.filename)
    session_id = str(uuid.uuid4())[:8]
    run_dir = os.path.join(os.getcwd(), 'temp_runs', session_id)
    
    try:
        shutil.copytree(os.path.abspath('logic-repo'), run_dir)
        
        sales_dir = os.path.join(run_dir, 'sales')
        sheets_dir = os.path.join(sales_dir, 'sheets')
        scripts_dir = os.path.join(run_dir, 'scripts')
        ws_output_dir = os.path.join(run_dir, 'configs/nonApproved/WS')

        os.makedirs(sheets_dir, exist_ok=True)
        os.makedirs(ws_output_dir, exist_ok=True)

        # 1. Save uploaded file to /sales/sheets
        file.save(os.path.join(sheets_dir, original_name))

        # 2. STEP 1: Run the shell script (The "Magic Sales" part)
        shell_result = subprocess.run(
            ['sh', 'newMagicSales.sh', f'./sheets/{original_name}'], 
            cwd=sales_dir, 
            capture_output=True, 
            text=True
        )
        if shell_result.returncode != 0:
            return f"newMagicSales.sh failed: {shell_result.stderr}", 500

        # 3. STEP 2: Move generated file from /sales to /scripts
        source_path = os.path.join(sales_dir, original_name)
        dest_path = os.path.join(scripts_dir, original_name)
        
        if not os.path.exists(source_path):
            return f"Error: Shell script finished but {original_name} was not found in {sales_dir}", 500
            
        shutil.move(source_path, dest_path)

        # 4. STEP 3: Run buildCfg.py using the Absolute Path
        abs_csv_path = os.path.abspath(dest_path)
        result = subprocess.run(
            ['python3', 'buildCfg.py', abs_csv_path], 
            cwd=scripts_dir, 
            capture_output=True, 
            text=True
        )

        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stdout, stderr=result.stderr)

        # 5. STEP 4: Zip and Send
        zip_base_name = os.path.join(run_dir, f"processed_{original_name.split('.')[0]}")
        zip_path = shutil.make_archive(zip_base_name, 'zip', ws_output_dir)

        return send_file(zip_path, as_attachment=True)
    
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Script Error: {e.stderr}"}), 500
        
    except Exception as e:
        return jsonify({"error": f"System Error: {str(e)}"}), 500
    finally:
        if os.path.exists(run_dir):
            shutil.rmtree(run_dir)

if __name__ == '__main__':
    app.run(port=5000, debug=True)