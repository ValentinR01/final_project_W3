<script lang=ts>
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';
  import TableProjects from '../../../components/organisms/TableProjects.svelte';
  import Searchbar from '../../../components/molecules/Searchbar.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';

  export let data;

  let rowElements : any = data.asset;

  let selectedRowElements: Array<any>;
  let selectedValues: Array<any>;

  export let role = 'user';
  export let domain = 'traducteur';

  // {title, has_high_priority, categorie, language, created_at, step_lifecycle, published_at, last_assignment_date, name_by_domain, rush_received, version, captation_done}: any) => ({ title, has_high_priority, categorie, language, created_at, step_lifecycle, published_at, last_assignment_date, name_by_domain, rush_received, version, captation_done }

  if (role === 'superadmin') {
    selectedRowElements = rowElements.map((
      { title, has_high_priority, categorie, step_lifecycle }: any) => ({ title, has_high_priority, categorie, step_lifecycle }
    ));
    selectedValues = selectedRowElements
  }

  if (role === 'admin') {
    selectedRowElements = rowElements.map((
      { title, has_high_priority, categorie, created_at, name_by_domain }: any) => ({ title, has_high_priority, categorie, created_at, name_by_domain }
    ));
    selectedValues = selectedRowElements
    if (domain === 'traducteur') {
      selectedRowElements = rowElements.map((
        { title, has_high_priority, categorie, language, created_at, name_by_domain }: any) => ({ title, has_high_priority, categorie, language, created_at, name_by_domain }
      ));
      selectedValues = selectedRowElements
    }
    if (domain === 'post-production') {
      selectedRowElements = rowElements.map((
        { title, has_high_priority, categorie, created_at, name_by_domain, rush_received }: any) => ({ title, has_high_priority, categorie, created_at, name_by_domain, rush_received }
      ));
      selectedValues = selectedRowElements
    }
  }

  if (role === 'user') {
    selectedRowElements = rowElements.map((
      { title, has_high_priority, categorie }: any) => ({ title, has_high_priority, categorie }
    ));
    selectedValues = selectedRowElements
    if (domain === 'régisseur') {
      selectedRowElements = rowElements.map((
        { title, has_high_priority, categorie, created_at, name_by_domain, captation_done }: any) => ({ title, has_high_priority, categorie, created_at, name_by_domain, captation_done }
      ));
      selectedValues = selectedRowElements
    }
  }


</script>

<div class='card block-center'>
  <Text
    textTag='h1'
    class='text-preset-1 text-center text--uppercase'
    >
    Vidéos en ligne
  </Text>
  
  <div class="table-container">
    <Margin marginTop='15px'>
      <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
    </Margin>

    <Margin marginTop='40px'>
      <TableProjects {selectedRowElements} />
    </Margin>
  </div>

  <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
</div>

<style>
  .table-container {
    display: table;
    margin-right: auto;
    margin-left: auto;
  }
  :global(.searchbar-container) {
    margin-right: 0;
    margin-left: auto;
  }
  :global(table) {
    display: table-row;
  }

</style>