C2-SERVER for linux

sudo apt update
sudo apt install nodejs npm

npm install -g ganache
pip install web3 py-solc-x

Project Architecture
                ┌────────────────────┐
                │  CVE Dataset / NVD │
                └─────────┬──────────┘
                          │
                          ▼
                    AI Engine
               (CVE Pattern Model)
                          │
                          ▼
                 Threat Intelligence
                          │
                          ▼
┌──────────────────────────────────────────┐
│         Blockchain Command Layer         │
│                                          │
│  Smart Contract                          │
│  - store command                         │
│  - store attack telemetry                │
│  - immutable log                         │
└─────────────────┬────────────────────────┘
                  │
                  ▼
          Research C2 Controller
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
 Simulation Agent 1      Simulation Agent 2
 (attack emulator)       (attack emulator)
