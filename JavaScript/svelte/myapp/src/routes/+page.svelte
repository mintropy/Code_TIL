<script lang="ts">
  import { onMount } from "svelte";

  onMount(() => {
    console.log("Page mounted");
  });

  let name: string = "SvelteKit";
</script>

<h1>Welcome to SvelteKit</h1>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the
  documentation
</p>
<p>
  Hello, {name}! This is your first SvelteKit page.
</p>
