<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import TextareaForm from "../../molecules/formFields/TextareaForm.svelte";

  export let typeBio = 'artist';

</script>

<form class='bio-edition'>
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase'
  > 
    Edition biographie
  </Text>
  <InputForm id="name" name="name"> 
    {#if typeBio == "artist"} 
      Nom de l’artiste
    {:else}
      Nom du compositeur
    {/if}
  </InputForm>
  <TextareaForm> Biographie </TextareaForm>
  <Button> Valider </Button>  
</form>

<style>
  .bio-edition{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    row-gap: var(--spacing-3);
  }
</style>