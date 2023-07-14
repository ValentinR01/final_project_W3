<script>
  import Text from "../../components/atoms/Text.svelte";
  import Searchbar from "../../components/molecules/Searchbar.svelte";
  import Pagination from '../../components/atoms/Pagination.svelte';

  /**
    * @type { any }
  */
  export let data;

  /**
   * @type {any}
  */
  let values;

</script>

<Text
  textTag='h2'
  class='text-preset-2'
  textColor='grey'
>
  Mettre dashboard
</Text>
<Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
<Pagination rows={data.asset} perPage={5} bind:trimmedRows={values} />