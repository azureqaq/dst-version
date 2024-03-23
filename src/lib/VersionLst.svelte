<script>
    import { onMount } from "svelte";
    const endpoint = "/dst-version/versions.json";

    let data = [];

    onMount(async function () {
        const response = await fetch(endpoint);
        const j = await response.json();
        data = j;
    });
</script>

<ul>
    {#each data as item}
        <li>
            version:
            <span class="version">
                {item.version}
            </span>
            date:
            <span class="date">
                {item.release_date}
            </span>
            {#if item.is_release}
                <span style="color: darkgreen;">Release</span>
            {:else}
                <span style="color: brown;">Test</span>
            {/if}
            {#if item.is_hotfix}
                <span style="color: darkorange;">Hotfix</span>
            {/if}
            {#if item.is_pinned}
                <span style="color: darkred;">Pinned</span>
            {/if}
        </li>
    {/each}
</ul>

<style>
    .version {
        color: darkgreen;
    }

    ul li {
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
