<script>
  import Text from '../../../components/atoms/Text.svelte';
  import Tabs from '../../../components/molecules/Tabs.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';

  import RegularOngoing from '../../../tabs/RegularOngoing.svelte';
  import RegularToStart from '../../../tabs/RegularToStart.svelte';
  import Link from '../../../components/atoms/Link.svelte';

  let domain = 'regisseur';
  export let data;

  let items = [
    { label: "A commencer",
     value: 1,
     component: RegularToStart
    },
    { label: "En cours",
     value: 2,
     component: RegularOngoing
    }
  ];
</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <Text
      textTag='h1'
      class='text-preset-1 text-center text--uppercase'
      >
      Les projets
    </Text>
  
    {#if domain == 'regisseur'}
      <Link linkUrl='/projects/create' linkColor='white' class='link--button'> + Nouveau projet </Link>
      <p> TABLEAU A AJOUTER </p>
      <p> DEUXIEME TABLEAU A AJOUTER </p>
    {:else}
      <div class='dashboard-nav'>
        <Tabs {items} data={data}/>
      </div>
    {/if}
  
  </div>
</Margin>

<style>
  .dashboard-nav{
    position: relative;
    margin-top: var(--spacing-5);
  }
</style>