<svelte:head>
	<title>Logged</title>
	<meta name="description" content="Logged" />
</svelte:head>

<script>
	import { onMount } from 'svelte';
	let api_response = '';
    function getCookie(cookieName) {
        let cookie = {};
        document.cookie.split(';').forEach(function(el) {
            let [key,value] = el.split('=');
            cookie[key.trim()] = value;
        })
        return cookie[cookieName];
    }
	async function getAPI() {
        const response = await fetch('https://localhost:8008/user', {
            method: 'GET',
            headers: { 'Content-type': 'application/json' }
        });
        let api_response = await response.json()
    return api_response.message
};
	onMount(async () => {
		api_response = getCookie("Authorization");
	});

</script>

<div>
    <p>user is: {api_response}</p>
</div>