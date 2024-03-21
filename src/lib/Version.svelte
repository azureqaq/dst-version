<script>
    import { onMount } from "svelte";
    const endpoint = "/dst-version/version.txt";

    let data = "...";

    onMount(async function () {
        const response = await fetch(endpoint);
        const t = await response.text();
        data = t.trim();
    });
</script>

<p>Version: {data}</p>
