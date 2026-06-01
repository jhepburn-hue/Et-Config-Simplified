module.exports = {
  packagerConfig: {
    asar: {
      unpackDir: 'logic-repo'
    },
    ignore: [
      /^\/temp_runs/,
      /^\/uploads/,
      /\.git/,
      /^\/venv/
    ]
  },
  rebuildConfig: {},
  makers: [
    {
      name: '@electron-forge/maker-squirrel', 
      config: {}
    },
    {
      name: '@electron-forge/maker-zip', 
      platforms: ['darwin']
    }
  ]
};