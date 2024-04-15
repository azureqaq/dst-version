<script>
    import { onMount } from "svelte";
    const endpoint = "/versions.json";

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
            <!-- version: -->
            <span class="version">
                {item.version}
            </span>
            &nbsp;
            <span class="date">
                {item.release_date}
            </span>
            &nbsp;
            {#if item.is_release}
                <span style="color: #7601bd;">Release</span>
            {:else}
                <span style="color: brown;">Test</span>
            {/if}
            {#if item.is_hotfix}
                <span style="color: darkorange;">Hotfix</span>
            {/if}
            {#if item.is_pinned}
                <span style="color: darkred;"><em>Pinned</em></span>
            {/if}
        </li>
    {/each}
</ul>

<style>
    .version {
        color: darkgreen;
        font-size: larger;
    }

    ul li {
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
