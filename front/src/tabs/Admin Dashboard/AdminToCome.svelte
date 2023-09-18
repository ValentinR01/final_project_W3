<script lang="ts">
  import Searchbar from "../../components/molecules/Searchbar.svelte";
  import Pagination from '../../components/atoms/Pagination.svelte';
  import TableProjects from '../../components/organisms/TableProjects.svelte';
  import Margin from '../../components/atoms/Margin.svelte';

  export let data : any;

  let domain = 'traducteur';

  let rowElements : any = data.asset;
  let selectedRowElements: Array<any>;
  let selectedValues: Array<any>;
    
  selectedRowElements = rowElements.map((
    { title, has_high_priority, categorie, created_at }: any) => ({ title, has_high_priority, categorie, created_at}
  ));
  selectedValues = selectedRowElements

  if (domain === 'traducteur') {
    selectedRowElements = rowElements.map((
      { title, has_high_priority, categorie, language, created_at }: any) => ({ title, has_high_priority, categorie, language, created_at }
    ));
    selectedValues = selectedRowElements
  }
</script>

<div class="table-container">
  <Margin marginTop='40px'>
    <TableProjects {selectedRowElements} />
  </Margin>

  <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
  <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
</div>
