<script>
import {Modal, Content, Trigger} from "sv-popup"
const githubClientId = "...";
const githubLink = `https://github.com/login/oauth/authorize?client_id=${githubClientId}&scope=user:email`;
</script>

<div>
    <h2>Github login</h2>
    <a href="{githubLink}" class="github">Login with Github</a>
</div>