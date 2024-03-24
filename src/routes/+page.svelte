<script>
    import Version from "$lib/Version.svelte";
    import VersionLst from "$lib/VersionLst.svelte";
</script>

<h1>DST Version</h1>
<hr />
Get DST version number every two hours from&nbsp;<a
    href="https://forums.kleientertainment.com/game-updates/dst/"
    >Klei&nbsp;forum</a
>.

<h2>Current Release</h2>
<hr />

<Version />

<h2>Recent Versions</h2>
<hr />
<VersionLst />

<h2>API</h2>
<hr />
<p>
    Current Release: <a href="version.txt">version.txt</a>
</p>
<p>Recent Versions: <a href="versions.json">versions.json</a></p>

<h2>Additional information</h2>
<hr />
<ul>
    <li>
        Github Repo: <a href="https://github.com/azureqaq/dst-version"
            >dst-version</a
        >
    </li>
    <li>
        Klei's Official Website: <a href="https://www.klei.com/">Klei</a>
    </li>
    <li>LICENSE: <a href="https://3moredays.mit-license.org/">MIT</a></li>
</ul>
