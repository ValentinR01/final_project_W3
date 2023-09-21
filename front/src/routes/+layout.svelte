<script>
  import '../assets/css/global.css';

  import Header from "../components/organisms/Header.svelte";
  
  import { onMount } from 'svelte';
  import { goto } from "$app/navigation";
  import { user } from "../store";

  export let data;

  user.set({ domain: data.cookies_domain, role: "superadmin", authentification: data.cookies_connexion});

  let url = ``;
  //if(data.cookies_connexion){
  //  user.set({ domain: data.cookies_domain, role: data.cookies_role, authentification: data.cookies_connexion});
  //}

  onMount(async () =>{
    url = window.location.href;

    if (!$user) {
      goto("/login");
    } else {
      console.log("User connected");
    }
  })
</script>

{#if url.includes('login')}
  <br>
{:else if $user}
  <Header />
{/if}

<div class='main'>
  <slot></slot>
</div>

<style>
  .main{
    height: calc(100vh - 90px);
    display: flex;
    align-items: center;
  }

  :global(.card){
    width: 60%;
    max-height: 500px;
    background-color: var(--color-background-secondary);
    padding: var(--spacing-5) var(--spacing-6);
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