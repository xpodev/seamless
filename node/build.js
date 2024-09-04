const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const nextVersion = process.argv[2];

execSync('yarn build:browser');

const packagesDir = path.join(__dirname, 'packages');
const packages = fs.readdirSync(packagesDir);
packages.forEach((pkg) => {
  const pkgPath = path.join(packagesDir, pkg);
  if (!fs.lstatSync(pkgPath).isDirectory()) {
    return;
  }
  const pkgJsonPath = path.join(pkgPath, 'package.json');
  const pkgJson = require(pkgJsonPath);
  pkgJson.version = nextVersion;
  fs.writeFileSync(pkgJsonPath, JSON.stringify(pkgJson, null, 2));
  execSync(`cd ${pkgPath} && npm run build && npm publish --access public`);
});
