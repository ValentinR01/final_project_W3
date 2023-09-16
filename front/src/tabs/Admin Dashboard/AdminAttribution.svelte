<script lang="ts">
  import Searchbar from "../../components/molecules/Searchbar.svelte";
  import Pagination from '../../components/atoms/Pagination.svelte';
  import TableProjects from '../../components/organisms/TableProjects.svelte';
  import Margin from '../../components/atoms/Margin.svelte';

  let domain = 'traducteur';

  export let data : any;

  let rowElements : any = data.asset;
  let selectedRowElements: Array<any>;
  let selectedValues: Array<any>;

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
  if (domain === 'post-prod') {
    selectedRowElements = rowElements.map((
      { title, has_high_priority, categorie, created_at, name_by_domain, rush_received }: any) => ({ title, has_high_priority, categorie, created_at, name_by_domain, rush_received }
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
