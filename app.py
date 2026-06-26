import os
import shutil
import subprocess
import uuid
from flask import Flask, request, render_template, send_file, jsonify
from werkzeug.utils import secure_filename
import sys

def get_base_path():
    if 'app.asar' in os.getcwd():
        return os.getcwd().replace('app.asar', 'app.asar.unpacked')
    return os.getcwd()

app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)
os.makedirs('temp_runs', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def run_pipeline():
    file = request.files.get('file')
    mode = request.form.get('mode', 'full') 
    
    if not file or file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    original_name = secure_filename(file.filename)
    base_filename = original_name.rsplit('.', 1)[0]
    session_id = str(uuid.uuid4())[:8]
    run_dir = os.path.join(os.getcwd(), 'temp_runs', session_id)
    
    try:
        shutil.copytree(os.path.join(get_base_path(), 'logic-repo'), run_dir)
        
        sales_dir = os.path.join(run_dir, 'sales')
        sheets_dir = os.path.join(sales_dir, 'sheets')
        scripts_dir = os.path.join(run_dir, 'scripts')
        ws_output_dir = os.path.join(run_dir, 'configs/nonApproved/WS')

        os.makedirs(sheets_dir, exist_ok=True)
        os.makedirs(ws_output_dir, exist_ok=True)

        # Dynamic Name Suffixes Based on Selection
        if mode == 'sales_only':
            export_name = f"{base_filename}_EDITABLE.csv"
        elif mode == 'build_only':
            export_name = f"{base_filename}_CONFIGS.zip"
        else:
            export_name = f"{base_filename}_FULL_PIPELINE.zip"

        # Setup File Routing & Save
        if mode == 'build_only':
            uploaded_file_path = os.path.join(scripts_dir, original_name)
            generated_filename = original_name
        else:
            uploaded_file_path = os.path.join(sheets_dir, original_name)
            
        # Save the file stream once so it writes full contents
        file.save(uploaded_file_path)

        # Extract Config Name from CSV Headers
        config_name = None
        try:
            import csv
            with open(uploaded_file_path, mode='r', encoding='utf-8', errors='ignore') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and "Config Name" in row[0]:
                        config_name = row[1].strip()
                        break
        except Exception as csv_err:
            return jsonify({"error": f"Failed to parse CSV headers: {str(csv_err)}"}), 400

        if not config_name:
            config_name = base_filename
        
        if mode != 'build_only':
            generated_filename = f"{config_name}.csv"

        # STEP 1: Run Magic Sales Script (Option 1 & Option 2)
        if mode in ['full', 'sales_only']:
            shell_result = subprocess.run(
                ['sh', 'newMagicSales.sh', f'./sheets/{original_name}'], 
                cwd=sales_dir, 
                capture_output=True, 
                text=True
            )
            if shell_result.returncode != 0:
                return jsonify({"error": f"newMagicSales.sh failed: {shell_result.stderr}"}), 500

            source_path = os.path.join(sales_dir, generated_filename)
            if not os.path.exists(source_path):
                return jsonify({"error": f"Shell script finished but {generated_filename} was not found in {sales_dir}"}), 500

            # If user ONLY wants the intermediate CSV, send it back immediately
            if mode == 'sales_only':
                # We need a persistent copy to send outside the try/finally cleanup block
                out_csv_path = os.path.join(os.getcwd(), 'uploads', f"edited_{generated_filename}")
                shutil.copy(source_path, out_csv_path)
                return send_file(out_csv_path, as_attachment=True, download_name=f"edited_{generated_filename}")

            # If Full Pipeline, move intermediate CSV to scripts folder for step 2
            dest_path = os.path.join(scripts_dir, generated_filename)
            shutil.move(source_path, dest_path)

        # STEP 2: Run Build Config Script (Option 1 & Option 3)
        if mode in ['full', 'build_only']:
            target_csv = os.path.join(scripts_dir, generated_filename)
            abs_csv_path = os.path.abspath(target_csv)
            
            result = subprocess.run(
                ['python3', 'buildCfg.py', abs_csv_path], 
                cwd=scripts_dir, 
                capture_output=True, 
                text=True
            )

            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stdout, stderr=result.stderr)

            # Zip and Send configurations
            zip_base_name = os.path.join(run_dir, f"processed_{config_name}")
            zip_path = shutil.make_archive(zip_base_name, 'zip', ws_output_dir)

            # Copy zip out of run_dir to safely send it without cleanup race conditions
            out_zip_path = os.path.join(os.getcwd(), 'uploads', f"processed_{config_name}.zip")
            shutil.copy(zip_path, out_zip_path)
            
            return send_file(out_zip_path, as_attachment=True, download_name=f"processed_{config_name}.zip")
    
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Script Error: {e.stderr if e.stderr else e.output}"}), 500
        
    except Exception as e:
        return jsonify({"error": f"System Error: {str(e)}"}), 500
    finally:
        if os.path.exists(run_dir):
            shutil.rmtree(run_dir)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)