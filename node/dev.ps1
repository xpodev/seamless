yarn build:browser
Copy-Item -Path ./packages/core/umd/index.js -Destination ../tests/server/static/main.js
Add-Content -Path ../tests/server/static/main.js -Value "const s = new Seamless.default();"
Copy-Item -Path ../tests/server/static/main.js -Destination ../examples/simple/static/main.js