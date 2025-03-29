import { execSync } from 'child_process';

const packagesDir = path.join(__dirname, 'packages');
const packages = fs.readdirSync(packagesDir);
packages.forEach((pkg) => {
  const pkgPath = path.join(packagesDir, pkg);
  if (!fs.lstatSync(pkgPath).isDirectory()) {
    return;
  }
  execSync(`cd ${pkgPath} && npm run build && npm publish --access public`);
});
