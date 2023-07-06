<script>

  import ModalCard from "../../molecules/cards/ModalCard.svelte";
  import Text from "../../atoms/Text.svelte";
  import IntervenorCreation from "../Forms/IntervenorCreation.svelte";

  export let type = 'intervenor';

</script>

<ModalCard buttonText='Ouvrir modale création intervenant'>
  <Text
    textTag='h2'
    class='text-preset-2 text--uppercase text-center'
  >
    {#if type == 'intervenor'}
      Nouvel intervenant
    {:else if type == 'composer'}
      Nouveau compositeur
    {/if}
  </Text>

  <IntervenorCreation data=any />

</ModalCard>