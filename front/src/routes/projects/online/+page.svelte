<script>
  import Margin from '../../../components/atoms/Margin.svelte';
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';

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
      Vidéos en ligne
    </Text>
  
    <p> REMPLACER PAR TABLEAU </p>
  
    <Pagination rows={data.metadata.instruments} perPage={3} bind:trimmedRows={values} />
  </div>
</Margin>