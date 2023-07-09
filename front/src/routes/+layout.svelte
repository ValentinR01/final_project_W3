<script>
  import '../assets/css/global.css';

  import Header from "../components/organisms/Header.svelte";
</script>

<Header />

<slot></slot>

<style>
  :global(.card){
    width: 60%;
    height: 500px;
    margin-top: 4%;
    background-color: var(--color-background-secondary);
    padding: var(--spacing-5) var(--spacing-6);
    border-radius: var(--card-radius);
  }

  :global(.tabs) :global(.searchbar-container){
    position: absolute;
    right: 0;
    top: -5px;
  }
</style>