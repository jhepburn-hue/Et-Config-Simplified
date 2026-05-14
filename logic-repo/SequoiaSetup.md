# Sequoia

## Sequoia Test instance

1. checkout the sequoia-server repo
2. go into the certs dir and run ./generate.sh
3. modify sequoia.py with the desired port
4. modify runserver.sh with the desired DB path.
5. remove any old sequoia DB if desired. (must run seq server clear to rebuild the db)
6. execute ./runserver.sh
7. 

## Sequoia scripts setup.

1. checkout the sequoia-scripts repo
2. modify the config.json to use the address and port that were configured for the server instance
   - All paths must end in a /
   - change the output: to an existing fully pathed output dir. 
   - change the left drive and right drive to the appropriate paths
3. run ./seq init -f config.json
4. if adding new keys
   1. generate any test data sets ./seq gen -n 10000 -c 250 -t templates/leave_3_0.template
   2. onboard any keys ./seq onboard -f *.keyfile
   3. ./seq server clear
   4. ./seq server sync
5. if no keys just unlock
   1. ./seq server unlock



## Config building

1. checkout the et-config repository
2. cd into scripts run the appropriate script.
   1. python3 buildCard.py
   2. python3 buildconfig.py <filename>