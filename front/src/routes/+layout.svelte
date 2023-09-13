<script>
  import '../assets/css/global.css';

  import Header from "../components/organisms/Header.svelte";
  
  import { onMount } from 'svelte';

  let url = ``;

  onMount(() => url = window.location.href)

  //let showHeader = true;
  //var currentURL = window.location.href;
  //if(currentURL.includes("login")){
  //  showHeader = false;
  //}

</script>

{#if url.includes("login")}
  <br>
{:else}
  <Header />
{/if}

<slot></slot>

<style>
  :global(.card){
    width: 60%;
    max-height: 500px;
    background-color: var(--color-background-secondary);
    padding: var(--spacing-4) var(--spacing-5);
    border-radius: var(--card-radius);
  }

  :global(.card--wide){
    max-height: 100%;
    margin-bottom: var(--spacing-4);
  }

  :global(.tabs) :global(.searchbar-container){
    position: absolute;
    right: 0;
    top: -5px;
  }
</style>