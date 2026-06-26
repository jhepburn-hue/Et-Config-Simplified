const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonProcess;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 520,
    height: 700, 
    webPreferences: { nodeIntegration: false }
  });

  const pythonExec = process.platform === 'win32' ? 'python' : 'python3';
  pythonProcess = spawn(pythonExec, [path.join(__dirname, 'app.py')]);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python STDOUT: ${data}`);
  });
  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python STDERR: ${data}`);
  });

  setTimeout(() => {
    mainWindow.loadURL('http://127.0.0.1:5000');
  }, 2000);

  mainWindow.on('closed', () => { mainWindow = null; });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (pythonProcess) pythonProcess.kill();
  if (process.platform !== 'darwin') app.quit();
});