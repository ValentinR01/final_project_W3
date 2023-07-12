<script>

  import Margin from "../../atoms/Margin.svelte";
  import Text from "../../atoms/Text.svelte";

  /**
   * @type {any}
   */
   export let data;

</script>

<div class='card card-projectInfos block-center'>
  <Margin marginBottom='var(--spacing-2)' class='w-100'>
    <Text
      textTag='h1'
      class='text-preset-2 text--uppercase'
    >
      Interview de Laure Sulob
    </Text>
  </Margin>

  <Text textTag='p' class='text-preset-4 w-50'> Nom de l’intervenant : Sylvie Delaunay </Text>
  {#if data.projects[0].categorie == 'masterclass' }
    <Text textTag='p' class='text-preset-4 w-50'> Nom de l’élève : Sebastien Sandal </Text>
  {/if}
  <Text textTag='p' class='text-preset-4 w-50'> Nom du morceau / pièce :  We are your friends </Text>
  <Text textTag='p' class='text-preset-4 w-50'> Nom du compositeur : Mozart </Text>
  <Text textTag='p' class='text-preset-4 w-50'> Instrument(s) : Piano, Violon </Text>
</div>

<style>
  .card-projectInfos{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-2);
  }
</style>