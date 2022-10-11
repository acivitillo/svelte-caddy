# Building a Deploying a simple Svelte App

This repo is a quick run through to build and deploy a simple Svelte app using sveltekit. The deployment is done via Caddy on HTTPS.


## Certs for HTTPS

The Caddy Server is configured to work via HTTPS, for that you will need to create your own certification files.

Create the certifications using `mkcert` and put them inside `data/certs`.

You can check the `data/Caddyfile` to make sure you name the certs in the right way for Caddy Server to work.

## Build the Svelte site

Svelte is a **frontend** javascript asset served using static **HTML** files. In order to have the html files, we need to build the Svelte code first.

There is a script in `build_svelte_site.sh` to build the Svelte site and copy the static assets into `docker/www`. If the script doesn't work on your platform (mine is Linux Ubuntu), you can still read the code to understand how to build Svelte on your platform.

## Docker Compose

```bash
cd docker
docker-compose up
```

You should be able to see the Svelte site at https://localhost:81/

## Understanding the Svelte build process

Svelte is a compiler, as such it can compile to different target platforms. The easiest way to serve Svelte, especially if you have a simple SPA that queries an API, is to use `'@sveltejs/adapter-static'` instead of `'@sveltejs/adapter-auto'` which comes as a default. This way you can serve a Svelte app with Caddy. Check the `svelte.config.js` file.

In order for prerendering to work, you also need to add the `+layout.js` file in `routes` with the line `export const prerender = true;`.