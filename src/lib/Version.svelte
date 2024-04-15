<script>
    import { onMount } from "svelte";
    const endpoint = "/version.txt";

    let data = "...";

    onMount(async function () {
        const response = await fetch(endpoint);
        const t = await response.text();
        data = t.trim();
    });
</script>

<p id="current_version">
    <strong>{data}</strong>
</p>

<style>
    #current_version {
        color: darkgreen;
        font-size: larger;
    }
</style>
