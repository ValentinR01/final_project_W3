<script lang="ts">
  import Margin from "../../components/atoms/Margin.svelte";
  import Searchbar from "../../components/molecules/Searchbar.svelte";
  import Pagination from '../../components/atoms/Pagination.svelte';
  import TableProjects from '../../components/organisms/TableProjects.svelte';

  export let data : any;

  let rowElements : any = data.asset;

  let selectedRowElements = rowElements.map((
    { title, has_high_priority, categorie, step_lifecycle }: any) => ({ title, has_high_priority, categorie, step_lifecycle }
  ));
  let selectedValues = selectedRowElements


</script>

<div class="table-container">
  <Margin marginTop='40px'>
    <TableProjects {selectedRowElements} />
  </Margin>

  <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
  <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
</div>