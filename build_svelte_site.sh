cd frontend/svelte-app
npm install
npm run build
cd ..
cd ..
cp frontend/svelte-app/.svelte-kit/output/prerendered/pages/* docker/data/www
cp -r frontend/svelte-app/.svelte-kit/output/prerendered/* docker/data/www
cp -r frontend/svelte-app/.svelte-kit/output/client/_app docker/data/www
