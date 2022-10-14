<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores'
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	let api_response = '';
	const isBeta = $page.url.searchParams.has('beta');
	async function getAPI() {
    const response = await fetch('https://localhost:8008/', {
        method: 'GET',
        headers: { 'Content-type': 'application/json' }
    });
    let api_response = await response.json()
    return api_response.message
};
	onMount(async () => {
		api_response = JSON.stringify(await getAPI());
	});

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>Api response is: {api_response}
		and param value is: {isBeta}
	</h1>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>
		to your new<br />SvelteKit app
	</h1>

	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2>

	<Counter />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
