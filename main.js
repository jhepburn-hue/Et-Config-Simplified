const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonProcess;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 500,
    height: 650,
    webPreferences: { nodeIntegration: false }
  });

  // Launch the Python Flask backend server as a background process
  const pythonExec = process.platform === 'win32' ? 'python' : 'python3';
  pythonProcess = spawn(pythonExec, [path.join(__dirname, 'app.py')]);

  // Allow the Flask server 2 seconds to boot up before loading the UI window
  setTimeout(() => {
    mainWindow.loadURL('http://127.0.0.1:5000');
  }, 2000);

  mainWindow.on('closed', () => { mainWindow = null; });
}

app.on('ready', createWindow);

// Ensure the background Python process is killed when the GUI is closed
app.on('window-all-closed', () => {
  if (pythonProcess) pythonProcess.kill();
  if (process.platform !== 'darwin') app.quit();
});