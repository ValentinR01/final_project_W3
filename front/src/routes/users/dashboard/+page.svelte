<script>
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';
  import Searchbar from '../../../components/molecules/Searchbar.svelte';
  import Button from '../../../components/atoms/Button.svelte';
  import Link from '../../../components/atoms/Link.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';

  export let data;
  /**
   * @type {any}
   */
  let values;
</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <Text
      textTag='h1'
      class='text-preset-1 text-center text--uppercase'
      >
      Les utilisateurs
    </Text>
  
    <div class='dashboard-nav'>
      <Searchbar urlSearchbar="projects" data={data.users} widthSearchbar="190" />
      <Link linkUrl='/users/create' linkColor='white' class='link--button'> Ajouter </Link>
    </div>
  
    <p class='text-center'> REMPLACER PAR TABLEAU </p>
  
    <Pagination rows={data.users} perPage={5} bind:trimmedRows={values} />
  </div>
</Margin>

<style>
  .dashboard-nav{
    display: flex;
    justify-content: space-between;
    margin-top: var(--spacing-5);
  }
</style>