cd frontend/svelte-app
npm run build
cd ..
cd ..
rm -r docker/configs/www
mkdir docker/configs/www
cp frontend/svelte-app/.svelte-kit/output/prerendered/pages/* docker/configs/www
cp frontend/svelte-app/.svelte-kit/output/prerendered/* docker/configs/www
cp -r frontend/svelte-app/.svelte-kit/output/client/_app docker/configs/www