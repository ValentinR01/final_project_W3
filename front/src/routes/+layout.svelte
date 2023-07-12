<script>
  import '../assets/css/global.css';

  import Header from "../components/organisms/Header.svelte";
</script>

<Header />

<slot></slot>

<style>
  :global(.card){
    width: 60%;
    max-height: 500px;
    margin-top: 3%;
    background-color: var(--color-background-secondary);
    padding: var(--spacing-4) var(--spacing-5);
    border-radius: var(--card-radius);
  }

  :global(.card--wide){
    max-height: 100%;
  }

  :global(.tabs) :global(.searchbar-container){
    position: absolute;
    right: 0;
    top: -5px;
  }
</style>